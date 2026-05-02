from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import cv2
import base64
import numpy as np
from pathlib import Path
from yolo26_detector import YOLO26ClassroomDetector
from attendance_logger import AttendanceLogger

app = Flask(__name__)
CORS(app)

# Pure YOLO26 detector
detector = YOLO26ClassroomDetector()
logger = AttendanceLogger()

# Create upload directory
UPLOAD_DIR = Path('static/uploads')
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@app.route('/')
def index():
    """Render main dashboard"""
    return render_template('index.html')

@app.route('/detect_image', methods=['POST'])
def detect_image():
    """Handle image upload detection"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    # Save uploaded image
    filepath = UPLOAD_DIR / file.filename
    file.save(filepath)
    
    # Run detection
    results, annotated = detector.detect_image(str(filepath))
    
    # Save annotated image
    output_path = UPLOAD_DIR / f'annotated_{file.filename}'
    cv2.imwrite(str(output_path), annotated)
    
    # Log attendance
    log_file = logger.log_attendance(results['student_count'])
    
    return jsonify({
        'success': True,
        'results': results,
        'annotated_url': f'/static/uploads/annotated_{file.filename}',
        'log_file': log_file
    })

@app.route('/detect_webcam', methods=['POST'])
def detect_webcam():
    """Handle webcam frame detection"""
    data = request.json
    if 'frame' not in data:
        return jsonify({'error': 'No frame provided'}), 400
    
    # Decode base64 image
    img_data = base64.b64decode(data['frame'].split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Run detection
    results, annotated_frame = detector.detect_frame(frame)
    
    # Encode annotated frame
    _, buffer = cv2.imencode('.jpg', annotated_frame)
    annotated_b64 = base64.b64encode(buffer).decode('utf-8')
    
    return jsonify({
        'success': True,
        'results': results,
        'annotated_frame': f'data:image/jpeg;base64,{annotated_b64}'
    })

@app.route('/save_attendance', methods=['POST'])
def save_attendance():
    """Manually save attendance snapshot"""
    data = request.json
    log_file = logger.log_attendance(data.get('student_count', 0))
    return jsonify({'success': True, 'log_file': log_file})

@app.route('/get_logs', methods=['GET'])
def get_logs():
    """Get today's attendance logs"""
    logs = logger.get_today_logs()
    return jsonify({'logs': logs})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
