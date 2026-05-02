from ultralytics import YOLO
import cv2
import numpy as np
from collections import defaultdict

class YOLO26ClassroomDetector:
    """YOLO26n for counting + Custom model for behaviors"""
    
    def __init__(self):
        print("Loading models...")
        
        # YOLO26n for accurate person detection
        self.detection_model = YOLO('yolo26n.pt')
        
        # Your custom model for behaviors (improved - 82% accuracy)
        self.behavior_model = YOLO('runs/detect/runs/detect/train_continued/weights/best.pt')
        
        # Instance Segmentation
        self.segment_model = YOLO('yolo26n-seg.pt')
        
        # Pose Estimation
        self.pose_model = YOLO('yolo26n-pose.pt')
        
        # Tracking
        self.tracker_type = 'bytetrack.yaml'
        self.track_history = defaultdict(lambda: [])
        
        print("✓ YOLO26n models loaded!")
        print("✓ Custom behavior model loaded!")
        
    def detect_image(self, image_path):
        """Detect students using YOLO26n only"""
        
        # Read image to get dimensions for better processing
        img = cv2.imread(image_path)
        h, w = img.shape[:2]
        
        # Use larger image size for better detection
        img_size = 1280 if max(h, w) > 1000 else 640
        
        # Person detection with YOLO26 - OPTIMIZED
        detection_results = self.detection_model(
            image_path,
            conf=0.20,      # Lower threshold to catch more students
            iou=0.40,       # Lower IOU to avoid merging separate people
            classes=[0],    # Person class
            max_det=150,    # Higher limit for large classrooms
            imgsz=img_size,
            agnostic_nms=False,
            verbose=False
        )[0]
        
        # Segmentation for verification
        segment_results = self.segment_model(
            image_path,
            conf=0.20,
            iou=0.40,
            classes=[0],
            max_det=150,
            imgsz=img_size,
            verbose=False
        )[0]
        
        # Pose estimation
        pose_results = self.pose_model(
            image_path,
            conf=0.20,
            iou=0.40,
            max_det=150,
            imgsz=img_size,
            verbose=False
        )[0]
        
        # BEHAVIOR DETECTION with custom model
        behavior_results = self.behavior_model(
            image_path,
            conf=0.25,
            iou=0.45,
            max_det=150,
            imgsz=img_size,
            verbose=False
        )[0]
        
        # Filter out low-quality detections
        valid_boxes = []
        for box in detection_results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            box_w = x2 - x1
            box_h = y2 - y1
            conf = float(box.conf[0])
            
            # Filter criteria:
            # 1. Minimum size (avoid tiny false positives)
            # 2. Aspect ratio check (people are taller than wide)
            # 3. Confidence threshold
            min_size = 30
            if box_w > min_size and box_h > min_size and conf > 0.20:
                # Aspect ratio: height should be >= width for standing/sitting people
                aspect_ratio = box_h / box_w
                if 0.5 <= aspect_ratio <= 4.0:  # Reasonable human proportions
                    valid_boxes.append(box)
        
        student_count = len(valid_boxes)
        
        # Analyze poses for hand raising
        hand_raised_count = 0
        sitting_count = 0
        standing_count = 0
        
        if pose_results.keypoints is not None:
            for kpts in pose_results.keypoints.data:
                kpts_np = kpts.cpu().numpy()
                
                # Check for raised hands
                if self._is_hand_raised(kpts_np):
                    hand_raised_count += 1
                
                # Analyze posture
                posture = self._analyze_posture(kpts_np)
                if posture == 'sitting':
                    sitting_count += 1
                elif posture == 'standing':
                    standing_count += 1
        
        # Extract behavior detections from custom model
        behavior_breakdown = {}
        if behavior_results.boxes is not None and len(behavior_results.boxes) > 0:
            for box in behavior_results.boxes:
                cls_id = int(box.cls[0])
                cls_name = behavior_results.names[cls_id]
                
                # Count each behavior
                if cls_name in behavior_breakdown:
                    behavior_breakdown[cls_name] += 1
                else:
                    behavior_breakdown[cls_name] = 1
        
        results = {
            'student_count': student_count,
            'behaviors': {
                'count': len(behavior_results.boxes) if behavior_results.boxes else 0,
                'breakdown': behavior_breakdown
            },
            'poses': {
                'pose_count': len(pose_results.keypoints) if pose_results.keypoints else 0,
                'hand_raised_count': hand_raised_count,
                'postures': {
                    'sitting': sitting_count,
                    'standing': standing_count
                }
            },
            'segmentation': {
                'mask_count': len(segment_results.masks) if segment_results.masks else 0
            }
        }
        
        # Draw visualization
        annotated = self._draw_detection(
            img,
            valid_boxes,
            pose_results,
            segment_results,
            behavior_results
        )
        
        return results, annotated
    
    def detect_frame(self, frame):
        """Detect in video frame with tracking"""
        
        h, w = frame.shape[:2]
        img_size = 1280 if max(h, w) > 1000 else 640
        
        # Object tracking with YOLO26 - OPTIMIZED
        track_results = self.detection_model.track(
            frame,
            conf=0.20,
            iou=0.40,
            classes=[0],
            persist=True,
            tracker=self.tracker_type,
            max_det=150,
            imgsz=img_size,
            agnostic_nms=False,
            verbose=False
        )[0]
        
        # Pose estimation
        pose_results = self.pose_model(
            frame,
            conf=0.20,
            iou=0.40,
            max_det=150,
            imgsz=img_size,
            verbose=False
        )[0]
        
        # Behavior detection with custom model
        behavior_results = self.behavior_model(
            frame,
            conf=0.25,
            iou=0.45,
            max_det=150,
            imgsz=img_size,
            verbose=False
        )[0]
        
        # Segmentation
        segment_results = self.segment_model(
            frame,
            conf=0.20,
            iou=0.40,
            classes=[0],
            max_det=150,
            imgsz=img_size,
            verbose=False
        )[0]
        
        # Filter valid detections
        valid_boxes = []
        for box in track_results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            box_w = x2 - x1
            box_h = y2 - y1
            conf = float(box.conf[0])
            
            min_size = 30
            if box_w > min_size and box_h > min_size and conf > 0.20:
                aspect_ratio = box_h / box_w
                if 0.5 <= aspect_ratio <= 4.0:
                    valid_boxes.append(box)
        
        student_count = len(valid_boxes)
        
        # Analyze poses
        hand_raised_count = 0
        if pose_results.keypoints is not None:
            for kpts in pose_results.keypoints.data:
                if self._is_hand_raised(kpts.cpu().numpy()):
                    hand_raised_count += 1
        
        # Extract behavior detections
        behavior_breakdown = {}
        if behavior_results.boxes is not None and len(behavior_results.boxes) > 0:
            for box in behavior_results.boxes:
                cls_id = int(box.cls[0])
                cls_name = behavior_results.names[cls_id]
                behavior_breakdown[cls_name] = behavior_breakdown.get(cls_name, 0) + 1
        
        # Process tracking - extract valid track IDs
        valid_track_ids = []
        if track_results.boxes.id is not None:
            all_track_ids = track_results.boxes.id.int().cpu().tolist()
            # Take only the IDs corresponding to valid boxes
            valid_track_ids = all_track_ids[:len(valid_boxes)]
        
        # Process tracking - only valid tracks
        tracking_data = {'active_tracks': len(set(valid_track_ids)), 'track_ids': valid_track_ids}
        
        results = {
            'student_count': student_count,
            'behaviors': {
                'count': len(behavior_results.boxes) if behavior_results.boxes else 0,
                'breakdown': behavior_breakdown
            },
            'poses': {
                'pose_count': len(pose_results.keypoints) if pose_results.keypoints else 0,
                'hand_raised_count': hand_raised_count
            },
            'tracking': tracking_data
        }
        
        # Draw visualization
        annotated = self._draw_frame(
            frame,
            valid_boxes,
            valid_track_ids,
            pose_results,
            segment_results,
            behavior_results
        )
        
        return results, annotated
    
    def _is_hand_raised(self, keypoints):
        """Detect raised hand from pose keypoints"""
        if len(keypoints) < 17:
            return False
        
        nose = keypoints[0]
        left_wrist = keypoints[9]
        right_wrist = keypoints[10]
        left_shoulder = keypoints[5]
        right_shoulder = keypoints[6]
        
        # Check if wrist is above shoulder (hand raised)
        if left_wrist[2] > 0.5 and left_shoulder[2] > 0.5:
            if left_wrist[1] < left_shoulder[1] - 30:
                return True
        
        if right_wrist[2] > 0.5 and right_shoulder[2] > 0.5:
            if right_wrist[1] < right_shoulder[1] - 30:
                return True
        
        return False
    
    def _analyze_posture(self, keypoints):
        """Analyze sitting vs standing"""
        if len(keypoints) < 17:
            return 'unknown'
        
        left_shoulder = keypoints[5]
        right_shoulder = keypoints[6]
        left_hip = keypoints[11]
        right_hip = keypoints[12]
        
        if left_shoulder[2] < 0.5 or right_shoulder[2] < 0.5:
            return 'sitting'
        
        if left_hip[2] > 0.5 and right_hip[2] > 0.5:
            shoulder_y = (left_shoulder[1] + right_shoulder[1]) / 2
            hip_y = (left_hip[1] + right_hip[1]) / 2
            vertical_dist = abs(hip_y - shoulder_y)
            
            if vertical_dist > 100:
                return 'standing'
            else:
                return 'sitting'
        
        return 'sitting'
    
    def _draw_detection(self, frame, valid_boxes, pose_results, segment_results, behavior_results):
        """Draw clean visualization"""
        annotated = frame.copy()
        h, w = annotated.shape[:2]
        
        # Draw segmentation masks (light blue overlay)
        if segment_results.masks is not None:
            masks = segment_results.masks.data.cpu().numpy()
            for mask in masks:
                mask_resized = cv2.resize(mask, (w, h))
                color_mask = np.zeros_like(annotated)
                color_mask[mask_resized > 0.5] = [180, 220, 255]
                annotated = cv2.addWeighted(annotated, 1, color_mask, 0.25, 0)
        
        # Draw valid person boxes (GREEN) with numbering and confidence
        for i, box in enumerate(valid_boxes, 1):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            
            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
            # Number badge
            cv2.circle(annotated, (x1 + 20, y1 + 20), 18, (0, 255, 0), -1)
            cv2.putText(annotated, str(i), (x1 + 13, y1 + 28),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
            
            # Show confidence
            cv2.putText(annotated, f'{conf:.2f}', (x1, y1 - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Draw behavior detections (RED boxes with labels)
        if behavior_results.boxes is not None:
            for box in behavior_results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                cls_name = behavior_results.names[cls_id]
                
                # Red box for behaviors
                cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                # Label background
                label = f'{cls_name} {conf:.2f}'
                (label_w, label_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
                cv2.rectangle(annotated, (x1, y1 - label_h - 10), (x1 + label_w + 10, y1), (0, 0, 255), -1)
                cv2.putText(annotated, label, (x1 + 5, y1 - 5),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        # Draw pose skeletons (YELLOW)
        if pose_results.keypoints is not None:
            for kpts in pose_results.keypoints.data:
                kpts_np = kpts.cpu().numpy()
                
                # Draw keypoints
                for x, y, conf in kpts_np:
                    if conf > 0.5:
                        cv2.circle(annotated, (int(x), int(y)), 4, (0, 255, 255), -1)
                
                # Draw skeleton connections
                connections = [
                    (5, 6), (5, 7), (7, 9), (6, 8), (8, 10),
                    (5, 11), (6, 12), (11, 12),
                    (11, 13), (13, 15), (12, 14), (14, 16)
                ]
                for start, end in connections:
                    if kpts_np[start][2] > 0.5 and kpts_np[end][2] > 0.5:
                        pt1 = (int(kpts_np[start][0]), int(kpts_np[start][1]))
                        pt2 = (int(kpts_np[end][0]), int(kpts_np[end][1]))
                        cv2.line(annotated, pt1, pt2, (0, 255, 255), 2)
                
                # Highlight raised hands
                if self._is_hand_raised(kpts_np):
                    nose = kpts_np[0]
                    if nose[2] > 0.5:
                        cv2.circle(annotated, (int(nose[0]), int(nose[1])), 25, (0, 255, 255), 3)
        
        # Info overlay
        overlay = annotated.copy()
        cv2.rectangle(overlay, (0, 0), (w, 120), (0, 0, 0), -1)
        annotated = cv2.addWeighted(annotated, 0.75, overlay, 0.25, 0)
        
        # Display metrics
        cv2.putText(annotated, f'STUDENTS: {len(valid_boxes)}', 
                   (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.6, (0, 255, 0), 4)
        
        hand_count = sum(1 for kpts in pose_results.keypoints.data if self._is_hand_raised(kpts.cpu().numpy())) if pose_results.keypoints else 0
        if hand_count > 0:
            cv2.putText(annotated, f'HANDS RAISED: {hand_count}', 
                       (20, 95), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 255), 3)
        
        return annotated
    
    def _draw_frame(self, frame, valid_boxes, valid_track_ids, pose_results, segment_results, behavior_results):
        """Draw frame with tracking"""
        annotated = frame.copy()
        h, w = annotated.shape[:2]
        
        # Segmentation masks
        if segment_results.masks is not None:
            masks = segment_results.masks.data.cpu().numpy()
            for mask in masks:
                mask_resized = cv2.resize(mask, (w, h))
                color_mask = np.zeros_like(annotated)
                color_mask[mask_resized > 0.5] = [180, 220, 255]
                annotated = cv2.addWeighted(annotated, 1, color_mask, 0.25, 0)
        
        # Draw valid boxes with tracking IDs
        for i, box in enumerate(valid_boxes, 1):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            
            cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
            # Show ID if available
            if i <= len(valid_track_ids):
                track_id = valid_track_ids[i-1]
                cv2.putText(annotated, f'ID:{track_id} {conf:.2f}', (x1, y1 - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            else:
                cv2.putText(annotated, f'{conf:.2f}', (x1, y1 - 10),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Draw behavior detections (RED boxes)
        if behavior_results.boxes is not None:
            for box in behavior_results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                cls_name = behavior_results.names[cls_id]
                
                cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 0, 255), 2)
                
                label = f'{cls_name} {conf:.2f}'
                (label_w, label_h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                cv2.rectangle(annotated, (x1, y1 - label_h - 8), (x1 + label_w + 8, y1), (0, 0, 255), -1)
                cv2.putText(annotated, label, (x1 + 4, y1 - 4),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
                # Update and draw tracking trail
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                self.track_history[track_id].append(center)
                
                if len(self.track_history[track_id]) > 30:
                    self.track_history[track_id].pop(0)
                
                if len(self.track_history[track_id]) > 1:
                    pts = np.array(self.track_history[track_id], dtype=np.int32)
                    cv2.polylines(annotated, [pts], False, (0, 255, 255), 2)
        
        # Draw poses
        if pose_results.keypoints is not None:
            for kpts in pose_results.keypoints.data:
                kpts_np = kpts.cpu().numpy()
                
                # Keypoints
                for x, y, conf in kpts_np:
                    if conf > 0.5:
                        cv2.circle(annotated, (int(x), int(y)), 4, (255, 255, 0), -1)
                
                # Skeleton
                connections = [
                    (5, 6), (5, 7), (7, 9), (6, 8), (8, 10),
                    (5, 11), (6, 12), (11, 12),
                    (11, 13), (13, 15), (12, 14), (14, 16)
                ]
                for start, end in connections:
                    if kpts_np[start][2] > 0.5 and kpts_np[end][2] > 0.5:
                        pt1 = (int(kpts_np[start][0]), int(kpts_np[start][1]))
                        pt2 = (int(kpts_np[end][0]), int(kpts_np[end][1]))
                        cv2.line(annotated, pt1, pt2, (255, 255, 0), 2)
        
        # Info overlay
        overlay = annotated.copy()
        cv2.rectangle(overlay, (0, 0), (w, 100), (0, 0, 0), -1)
        annotated = cv2.addWeighted(annotated, 0.75, overlay, 0.25, 0)
        
        hand_count = sum(1 for kpts in pose_results.keypoints.data if self._is_hand_raised(kpts.cpu().numpy())) if pose_results.keypoints else 0
        
        cv2.putText(annotated, f'Students: {student_count}', 
                   (15, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 3)
        
        if hand_count > 0:
            cv2.putText(annotated, f'Hands: {hand_count}', 
                       (15, 85), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)
        
        return annotated
