<div align="center">

# 🎓 Smart Classroom Detector

### AI-Powered Classroom Monitoring & Behavior Analytics using Computer Vision

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/YOLO26-Object_Detection-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Gradio-Interactive_UI-FF6F00?style=for-the-badge&logo=gradio"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/HuggingFace-Deployed-FFD21E?style=for-the-badge&logo=huggingface"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Classes-5-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Computer_Vision-AI-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Education-Tech-purple?style=flat-square"/>
</p>

### Detect • Analyze • Monitor • Improve

An intelligent classroom monitoring system that uses Deep Learning, Object Detection, Pose Estimation, and Computer Vision to automatically analyze classroom activities and student engagement.

</div>

---

# 📖 Overview

Smart Classroom Detector is an AI-powered educational analytics platform designed to assist educators in understanding classroom dynamics through automated visual analysis.

The system utilizes multiple YOLO26 models for:

* Student Detection
* Human Pose Estimation
* Instance Segmentation
* Classroom Behavior Recognition
* Attendance Logging

The platform helps educators gain insights into student participation, attentiveness, and classroom engagement using real-time AI analysis.

---

# 🚀 Key Features

## 👥 Student Detection

* Real-time student detection
* Accurate student counting
* Multi-person recognition
* Classroom occupancy monitoring

---

## 🧠 Behavior Recognition

The system detects important classroom behaviors:

| Behavior       | Description                |
| -------------- | -------------------------- |
| ✋ Hand Raising | Student participation      |
| 😴 Sleeping    | Inattentiveness detection  |
| 📱 Phone Usage | Distraction identification |
| ✍️ Writing     | Note-taking activity       |
| 📖 Reading     | Learning engagement        |

---

## 🤸 Human Pose Estimation

* Student posture analysis
* Body keypoint detection
* Hand raise identification
* Activity understanding

---

## 🎭 Instance Segmentation

* Individual student segmentation
* Better object separation
* Enhanced classroom visualization

---

## 📝 Attendance Logging

* Automated attendance generation
* Timestamp recording
* CSV attendance storage
* Historical attendance tracking

---

## 📊 Classroom Analytics

* Student participation insights
* Behavior monitoring
* Classroom activity analysis
* Engagement tracking

---

# 🏗️ System Workflow

```text
Input Image / Classroom Feed
              │
              ▼
      YOLO26 Detection
              │
              ▼
      Student Counting
              │
              ▼
      Pose Estimation
              │
              ▼
     Behavior Detection
              │
              ▼
     Attendance Logging
              │
              ▼
      Analytics Output
```

---

# 📸 Project Showcase

## 🎨 User Interface

<img src="img/demo1.png" width="100%" />

---

## 🎯 Detection Results

<img src="img/demo2.png" width="100%" />

---

## 📹 Real-Time Monitoring

<img src="img/demo3.png" width="100%" />

---

# 🎯 Detected Behaviors

| Class        | Purpose                          |
| ------------ | -------------------------------- |
| Hand Raising | Measures classroom participation |
| Sleeping     | Detects inattentive students     |
| Phone Usage  | Identifies distractions          |
| Writing      | Tracks note-taking behavior      |
| Reading      | Measures learning engagement     |

---

# 🤖 AI Models Used

## YOLO26 Object Detection

Used for:

* Student Detection
* Classroom Occupancy Monitoring
* Object Localization

---

## YOLO26 Pose Estimation

Used for:

* Human Keypoint Detection
* Hand Raise Recognition
* Posture Analysis

---

## YOLO26 Segmentation

Used for:

* Individual Student Segmentation
* Enhanced Scene Understanding

---

# 💻 Technology Stack

## Programming Language

* Python

## Frontend

* Gradio

## Computer Vision

* OpenCV
* NumPy
* Pillow

## Deep Learning

* PyTorch
* Ultralytics YOLO26

## Data Processing

* Pandas

## Deployment

* Hugging Face Spaces

---

# 📂 Project Structure

```bash
AI-SmartClassroom-Detector/
│
├── app.py
├── attendance_logger.py
├── yolo26_detector.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── main.js
│
├── attendance_logs/
│
├── img/
│   ├── demo1.png
│   ├── demo2.png
│   └── demo3.png
│
├── yolo26n.pt
├── yolo26n-seg.pt
└── yolo26n-pose.pt
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/khushanuma-shabbir/AI-SmartClassroom-Detector.git

cd AI-SmartClassroom-Detector
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

---

# 🎮 Usage

### Step 1

Launch the application.

### Step 2

Upload a classroom image.

### Step 3

Run AI analysis.

### Step 4

View:

* Student Count
* Detected Behaviors
* Pose Analysis
* Attendance Records
* Visual Results

---

# 🌍 Applications

## 🏫 Educational Institutions

* Smart Attendance Systems
* Classroom Monitoring
* Student Engagement Analysis

## 📊 Academic Research

* Learning Behavior Studies
* Student Activity Analysis
* Classroom Analytics

## 🤖 Smart Education

* AI-Assisted Teaching
* Automated Monitoring
* Data-Driven Insights

---

# 🔮 Future Enhancements

* Multi-camera support
* Cloud database integration
* Advanced analytics dashboard
* Mobile application
* LMS integration
* Teacher alerts
* Report generation
* Smart classroom recommendations

---

# 🌐 Live Demo

### Hugging Face Space

https://huggingface.co/spaces/Khushanuma-shabbir/smart-classroom-detector

---

# 👩‍💻 Developer

## Khushanuma Shabbir Mansuri

**B.Tech Information Technology**

MPSTME, NMIMS University

### Interests

* Artificial Intelligence
* Machine Learning
* Computer Vision
* Data Analytics
* Full Stack Development

### Connect

GitHub:
https://github.com/khushanuma-shabbir

LinkedIn:
https://linkedin.com/in/khushanuma-shabbir

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the repository

🤝 Contribute to the project

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

### 🚀 Transforming Education with Artificial Intelligence

Smart Classroom Detector • Computer Vision • Deep Learning • Educational Analytics

</div>
