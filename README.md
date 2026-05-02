# 🎓 Smart Classroom Detector

AI-powered classroom monitoring system using YOLO26n for accurate student counting and custom behavior detection.

## Features

- 👥 **Accurate Student Counting** - YOLO26n person detection
- 📱 **Behavior Detection** - Phone usage, Writing, Reading, Sleeping
- ✋ **Hand Raising Detection** - Pose estimation
- 🎭 **Instance Segmentation** - Visual verification
- 📊 **Real-time Analytics** - Live dashboard
- 📝 **Attendance Logging** - CSV export
- 📹 **Webcam Support** - Live detection

## Tech Stack

- **Backend**: Flask, Python
- **AI Models**: YOLO26n, Custom trained model
- **Frontend**: HTML, CSS, JavaScript
- **Computer Vision**: OpenCV, Ultralytics

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/smart-classroom-detector.git
cd smart-classroom-detector
```

2. **Create virtual environment**
```bash
python -m venv yolo_env
source yolo_env/bin/activate  # Linux/Mac
# or
yolo_env\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open browser**
```
http://localhost:5000
```

## Usage

### Upload Image
1. Click "Choose File" and select a classroom image
2. Click "Detect Students"
3. View results with bounding boxes and analytics

### Webcam Detection
1. Click "Start Webcam"
2. Allow camera permissions
3. Real-time detection with tracking

### Save Attendance
1. After detection, click "Save Attendance"
2. Logs saved to `attendance_logs/` folder

## Project Structure

```
smart-classroom-detector/
├── app.py                      # Flask backend
├── yolo26_detector.py          # Main detector (YOLO26n + custom model)
├── attendance_logger.py        # Attendance logging
├── test_yolo26.py             # Test script
├── requirements.txt           # Dependencies
├── templates/
│   └── index.html            # Frontend UI
├── static/
│   ├── css/style.css         # Styling
│   ├── js/main.js            # Frontend logic
│   └── uploads/              # Uploaded images
├── attendance_logs/          # CSV logs
├── runs/detect/train4/       # Custom trained model
│   └── weights/best.pt
└── ClassRoom_Dataset/        # Training dataset
```

## Models

- **yolo26n.pt** - Person detection (student counting)
- **yolo26n-seg.pt** - Instance segmentation
- **yolo26n-pose.pt** - Pose estimation (hand raising)
- **best.pt** - Custom behavior model (phone, writing, reading, sleeping)

## Testing

```bash
python test_yolo26.py
```

## Deployment

See `DEPLOY_RENDER.md` for deployment instructions to Render (FREE).

## Requirements

- Python 3.8+
- Webcam (for live detection)
- 4GB+ RAM recommended

## License

MIT License

## Author

Your Name

## Acknowledgments

- Ultralytics YOLO
- Flask Framework
- OpenCV
