<div align="center">

# ✨ Smart Classroom Detector ✨

<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Smart Classroom AI" width="180" style="border-radius: 50%; box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);" />
</p>

<p align="center">
  <em>🎓 Transforming Education with AI-Powered Classroom Intelligence 🎓</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-FF69B4?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/YOLO-v11-9370DB?style=for-the-badge&logo=yolo&logoColor=white" alt="YOLO"/>
  <img src="https://img.shields.io/badge/Flask-2.0+-FF1493?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/OpenCV-4.8+-BA55D3?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-82%25-FF69B4?style=for-the-badge&logo=target&logoColor=white" alt="Accuracy"/>
  <img src="https://img.shields.io/badge/Status-Live-9370DB?style=for-the-badge&logo=statuspage&logoColor=white" alt="Status"/>
  <img src="https://img.shields.io/badge/Made_with-❤️-FF1493?style=for-the-badge" alt="Made with Love"/>
</p>

<p align="center">
  <a href="#-about-the-project">About</a> •
  <a href="#-live-demo">Demo</a> •
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-tech-stack">Tech Stack</a>
</p>

---

### 🌸 *"Empowering educators with intelligent classroom insights"* 🌸

</div>

## 💫 About The Project

**Smart Classroom Detector** is an innovative AI-powered system that revolutionizes how we monitor and understand classroom dynamics. Built with cutting-edge deep learning technology, this project automates attendance tracking, analyzes student behavior, and provides real-time insights to enhance the learning environment.

### 🎯 The Challenge

Traditional classroom management faces several critical issues:

<table>
<tr>
<td width="50%">

#### ⏰ Time Wastage
Manual attendance consumes **5-10 minutes** every class, disrupting the learning flow and reducing valuable teaching time.

#### 🚫 Proxy Attendance
Students can fraudulently mark absent peers as present with no way to detect or prevent this dishonest practice.

</td>
<td width="50%">

#### 📊 No Engagement Data
Teachers have zero visibility into student attentiveness, participation levels, or behavioral patterns during class.

#### 🔍 Lack of Analytics
Educational decisions rely on guesswork without real-time data, trends analysis, or actionable insights.

</td>
</tr>
</table>

### 💡 My Solution

An intelligent, real-time monitoring system that:

✨ **Automatically counts students** with 95%+ accuracy using YOLO26n  
✨ **Detects 5 key behaviors**: Hand Raising, Sleeping, Phone Usage, Writing, Reading  
✨ **Generates instant attendance logs** saved as CSV files  
✨ **Provides live analytics dashboard** with beautiful visualizations  
✨ **Works with images AND live webcam** for maximum flexibility  
✨ **Tracks student poses** to identify hand raising and posture  
✨ **Creates visual segmentation** for clear student identification  

---

## 🌐 Live Demo

<div align="center">

### 🚀 Experience It Live!

[![Hugging Face Spaces](https://img.shields.io/badge/🤗_Try_Live_Demo-Hugging_Face-FFD700?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/spaces/Khushanuma-shabbir/smart-classroom-detector)

**Or run locally at:** `http://localhost:5000`

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18,20&height=100&section=header&text=Click%20Above%20to%20Try!&fontSize=30&fontColor=fff&animation=twinkling"/>

</div>

---

## 📸 Project Showcase

<div align="center">

### 🎨 Beautiful User Interface

<img src="img/demo1.png" width="850" style="border-radius: 20px; box-shadow: 0 15px 50px rgba(147, 51, 234, 0.3); border: 3px solid #9333ea;" />

<p><em>✨ Elegant dashboard with real-time analytics and intuitive controls ✨</em></p>

<br/>

### 📹 Real-Time Webcam Monitoring

<img src="img/demo3.png" width="850" style="border-radius: 20px; box-shadow: 0 15px 50px rgba(139, 92, 246, 0.3); border: 3px solid #8b5cf6;" />

<p><em>🎥 Live classroom monitoring with instant behavioral analysis 🎥</em></p>

<br/>

### 🎯 AI-Powered Detection Results

<img src="img/demo2.png" width="850" style="border-radius: 20px; box-shadow: 0 15px 50px rgba(236, 72, 153, 0.3); border: 3px solid #ec4899;" />

<p><em>🤖 Advanced detection with bounding boxes, behavior labels, pose estimation & segmentation 🤖</em></p>

</div>

---

## ✨ Features

<div align="center">

### 🌟 Core Capabilities

</div>

<table>
<tr>
<td width="33%" align="center">

### 👥 Student Detection
**95%+ Accuracy**

Powered by YOLO26n for precise person counting in crowded classrooms

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135755.png" width="80"/>

</td>
<td width="33%" align="center">

### 🧠 Behavior Analysis
**82% Accuracy**

Custom-trained model detects 5 key student behaviors in real-time

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135768.png" width="80"/>

</td>
<td width="33%" align="center">

### 📊 Live Analytics
**Real-Time Dashboard**

Beautiful visualizations showing student count, behaviors, and engagement

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" width="80"/>

</td>
</tr>
</table>

### 🎯 Detected Behaviors

<div align="center">

| Behavior | Emoji | Detection Rate | Use Case |
|:--------:|:-----:|:--------------:|:--------:|
| **Hand Raising** | ✋ | 91.9% | Track participation |
| **Sleeping** | 😴 | 88.9% | Monitor attentiveness |
| **Using Phone** | 📱 | 82.0% | Identify distractions |
| **Writing** | ✍️ | 77.4% | Gauge note-taking |
| **Reading** | 📖 | 71.0% | Assess engagement |

</div>

### 🚀 Advanced Features

<table>
<tr>
<td width="50%">

#### 📷 Dual Detection Modes
- **Image Upload**: Analyze classroom photos instantly
- **Live Webcam**: Real-time monitoring with continuous detection
- **Flexible Input**: Works with any image format

#### 🎭 Multi-Model Architecture
- **YOLO26n**: Person detection (5.5 MB)
- **YOLO26n-seg**: Instance segmentation (6.7 MB)
- **YOLO26n-pose**: Pose estimation (7.0 MB)
- **Custom Model**: Behavior detection (5.4 MB, 82% accuracy)

</td>
<td width="50%">

#### 📝 Attendance Management
- **Automatic Logging**: CSV export with timestamps
- **Daily Records**: Organized by date
- **Manual Save**: Option to save specific snapshots
- **Historical Data**: View past attendance logs

#### 🎨 Beautiful Interface
- **Gradient Design**: Modern purple-pink theme
- **Responsive Layout**: Works on all screen sizes
- **Real-time Updates**: Live statistics dashboard
- **Intuitive Controls**: Easy-to-use buttons and inputs

</td>
</tr>
</table>

---

## 🏆 Model Performance

<div align="center">

### 📊 Accuracy Metrics

<img src="https://img.shields.io/badge/Overall_mAP@50-82.24%25-FF69B4?style=for-the-badge&logo=target&logoColor=white"/>
<img src="https://img.shields.io/badge/Student_Counting-95%25+-9370DB?style=for-the-badge&logo=checkmarx&logoColor=white"/>

<br/><br/>

| Behavior | Precision | Recall | mAP@50 | mAP@50-95 | Status |
|:--------:|:---------:|:------:|:------:|:---------:|:------:|
| **✋ Hand Raising** | 86.5% | 92.0% | **91.9%** | 53.1% | 🌟 Excellent |
| **😴 Sleeping** | 83.1% | 88.3% | **88.9%** | 46.9% | 🌟 Excellent |
| **📱 Using Phone** | 78.8% | 72.4% | **82.0%** | 48.4% | ✅ Very Good |
| **✍️ Writing** | 76.4% | 65.9% | **77.4%** | 48.3% | ✅ Good |
| **📖 Reading** | 66.2% | 63.9% | **71.0%** | 41.2% | ✅ Good |

### 🎓 Training Details

**Dataset**: 1,422 classroom images | **Epochs**: 50 | **Framework**: Ultralytics YOLOv11

</div>

---

## ⚙️ Tech Stack

<div align="center">

### 💻 Technologies Used

<table>
<tr>
<td align="center" width="20%">
<img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" width="70"/><br/>
<strong>Python 3.11+</strong><br/>
<em>Core Language</em>
</td>
<td align="center" width="20%">
<img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="110"/><br/>
<strong>YOLO26 (v11)</strong><br/>
<em>AI Detection</em>
</td>
<td align="center" width="20%">
<img src="https://cdn-icons-png.flaticon.com/512/1183/1183672.png" width="70"/><br/>
<strong>Flask</strong><br/>
<em>Web Framework</em>
</td>
<td align="center" width="20%">
<img src="https://cdn-icons-png.flaticon.com/512/919/919827.png" width="70"/><br/>
<strong>OpenCV</strong><br/>
<em>Computer Vision</em>
</td>
<td align="center" width="20%">
<img src="https://cdn-icons-png.flaticon.com/512/732/732212.png" width="70"/><br/>
<strong>HTML/CSS/JS</strong><br/>
<em>Frontend</em>
</td>
</tr>
</table>

### 📦 Complete Technology Stack

| Layer | Technologies |
|:-----:|:------------|
| **🎨 Frontend** | HTML5, CSS3 (Gradient Design), JavaScript (ES6+) |
| **⚙️ Backend** | Flask 2.0+, Python 3.11+, Flask-CORS |
| **🤖 AI/ML** | YOLO26n, PyTorch, Ultralytics, Custom Trained Model |
| **👁️ Computer Vision** | OpenCV 4.8+, NumPy, Pillow |
| **📊 Data** | Pandas, CSV, JSON |
| **🚀 Deployment** | Hugging Face Spaces, Gradio, Gunicorn |

</div>

---

## 🚀 Installation

### 📋 Prerequisites

- Python 3.11 or higher
- pip package manager
- Git
- Webcam (optional, for live detection)

### 💻 Step-by-Step Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/khushanuma-shabbir/AI-SmartClassroom-Detector.git
cd AI-SmartClassroom-Detector
```

#### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv yolo_env
yolo_env\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv yolo_env
source yolo_env/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Application

```bash
python app.py
```

#### 5️⃣ Open in Browser

Navigate to: **`http://localhost:5000`**

<div align="center">

🎉 **You're all set! Start detecting!** 🎉

</div>

---

## 💡 How It Works

<div align="center">

### 🔄 Detection Pipeline

</div>

```
📷 Input (Image/Webcam)
        ↓
🤖 YOLO26n Person Detection (95%+ accuracy)
        ↓
🎭 Instance Segmentation (Visual clarity)
        ↓
🤸 Pose Estimation (Hand raising detection)
        ↓
🧠 Custom Behavior Model (5 behaviors, 82% accuracy)
        ↓
📊 Analytics Processing
        ↓
🎨 Visualization & Results
        ↓
💾 Attendance Logging (CSV)
```

### 🎯 Detection Process

<table>
<tr>
<td width="50%">

#### 📷 Image Detection Mode

1. **Upload** classroom image
2. **Process** through 4 AI models simultaneously
3. **Filter** detections using aspect ratio & confidence
4. **Analyze** poses for hand raising
5. **Detect** behaviors (phone, sleeping, etc.)
6. **Visualize** with bounding boxes & labels
7. **Display** results on dashboard
8. **Save** attendance log automatically

</td>
<td width="50%">

#### 🎥 Webcam Detection Mode

1. **Start** webcam stream
2. **Capture** frames every second
3. **Track** students with ByteTrack algorithm
4. **Detect** behaviors in real-time
5. **Update** analytics dashboard live
6. **Show** annotated video feed
7. **Monitor** continuously
8. **Save** attendance on demand

</td>
</tr>
</table>

---

## 📁 Project Structure

```
AI-SmartClassroom-Detector/
│
├── 📄 app.py                          # Flask application with 6 routes
├── 🤖 yolo26_detector.py              # Detection engine (4 models)
├── 📝 attendance_logger.py            # CSV attendance tracking
├── 📋 requirements.txt                # 7 core dependencies
├── 📖 README.md                       # This beautiful file!
├── 🚀 DEPLOY_HF_STEPS.md             # Deployment guide
├── 🔒 .gitignore                      # Git configuration
│
├── 📂 templates/
│   └── index.html                     # Main web interface (200+ lines)
│
├── 📂 static/
│   ├── css/
│   │   └── style.css                  # Gradient purple-pink theme
│   └── js/
│       └── main.js                    # Frontend logic (300+ lines)
│
├── 📂 runs/
│   └── detect/
│       └── train_continued/
│           └── weights/
│               └── best.pt            # Custom model (82% accuracy)
│
├── 📂 ClassRoom_Dataset/              # Training data
│   ├── train/                         # 1,245 images
│   ├── test/                          # 177 images
│   └── valid/                         # 177 images
│
├── 📂 attendance_logs/                # CSV attendance records
│
└── 🎯 Model Files
    ├── yolo26n.pt                     # Person detection (5.5 MB)
    ├── yolo26n-seg.pt                 # Segmentation (6.7 MB)
    └── yolo26n-pose.pt                # Pose estimation (7.0 MB)
```

---

## 🎯 Use Cases

<div align="center">

<table>
<tr>
<td width="33%" align="center">

### 🏫 Education

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="80"/>

- Automated attendance
- Engagement monitoring
- Participation tracking
- Behavior analysis
- Learning analytics

</td>
<td width="33%" align="center">

### 📊 Analytics

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" width="80"/>

- Classroom insights
- Trend analysis
- Performance metrics
- Data-driven decisions
- Predictive analytics

</td>
<td width="33%" align="center">

### 🔒 Safety

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135768.png" width="80"/>

- Real-time monitoring
- Anomaly detection
- Safety compliance
- Incident reporting
- Security alerts

</td>
</tr>
</table>

</div>

---

## 🛣️ Future Roadmap

<div align="center">

### 🌟 Planned Enhancements

</div>

- [ ] 📱 **Mobile App** - iOS & Android native applications
- [ ] 🎥 **Multi-Camera Support** - Monitor multiple classrooms simultaneously
- [ ] ☁️ **Cloud Database** - MongoDB/PostgreSQL integration
- [ ] 📧 **Smart Alerts** - Email/SMS notifications for teachers
- [ ] 🎨 **Advanced Dashboard** - More visualizations and insights
- [ ] 🌐 **LMS Integration** - Connect with Moodle, Canvas, Blackboard
- [ ] 🗣️ **Multi-Language** - Support for multiple languages
- [ ] 🔌 **REST API** - Third-party integration capabilities
- [ ] 📈 **Predictive Analytics** - ML-based student performance prediction
- [ ] 🎓 **Student Recognition** - Face recognition for individual tracking

---

## 🧑‍💻 About the Developer

<div align="center">

<img src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" width="120" style="border-radius: 50%; border: 4px solid #9333ea; box-shadow: 0 10px 30px rgba(147, 51, 234, 0.3);"/>

### **Khushanuma Shabbir Mansuri**

🎓 **B.Tech in Information Technology**  
🏛️ **NMIMS University, Mumbai**

💜 *Passionate about AI/ML, Computer Vision & Full-Stack Development*  
✨ *Building intelligent solutions to real-world problems*  
🌸 *Empowering education through technology*

<br/>

<p align="center">
  <a href="mailto:khushanuma.shabbir@gmail.com">
    <img src="https://img.shields.io/badge/Email-FF69B4?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/>
  </a>
  <a href="https://linkedin.com/in/khushanuma-shabbir">
    <img src="https://img.shields.io/badge/LinkedIn-9370DB?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <a href="https://github.com/khushanuma-shabbir">
    <img src="https://img.shields.io/badge/GitHub-FF1493?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>
</p>

</div>

---

## 🏆 Project Achievements

<div align="center">

<table>
<tr>
<td align="center" width="33%">

### 🎯 Technical Excellence

✅ Built complete full-stack AI application  
✅ Integrated 4 YOLO models seamlessly  
✅ Achieved 82% behavior detection accuracy  
✅ Processed 1,422 training images  
✅ Implemented real-time video processing  

</td>
<td align="center" width="33%">

### 🚀 Deployment Success

✅ Successfully deployed on Hugging Face  
✅ Created beautiful responsive UI  
✅ Implemented dual detection modes  
✅ Built attendance logging system  
✅ Optimized for production use  

</td>
<td align="center" width="33%">

### 💡 Innovation

✅ Hybrid multi-model architecture  
✅ Real-time pose estimation  
✅ Custom behavior detection  
✅ Automated attendance tracking  
✅ Live analytics dashboard  

</td>
</tr>
</table>

<br/>

### 📊 Project Statistics

<img src="https://img.shields.io/badge/Lines_of_Code-2000+-FF69B4?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Models_Integrated-4-9370DB?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Training_Images-1422-FF1493?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Detection_Speed-<2s-BA55D3?style=for-the-badge"/>

</div>

---

## 📄 License

<div align="center">

This project is licensed under the **MIT License**

Feel free to use, modify, and distribute this project with proper attribution.

</div>

---

## 💖 Support This Project

<div align="center">

If you find this project helpful and inspiring, please consider:

<br/>

⭐ **Star this repository** to show your support  
🍴 **Fork and contribute** to make it even better  
📢 **Share with others** who might benefit  
💬 **Provide feedback** to help improve  
🤝 **Connect with me** on LinkedIn

<br/>

### 🌸 Thank You for Your Support! 🌸

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18,20&height=120&section=footer&text=Made%20with%20💜%20by%20Khushanuma&fontSize=30&fontColor=fff&animation=twinkling"/>

</div>
