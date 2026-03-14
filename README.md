# AI Surveillance Dashboard

A **real time computer vision dashboard** built with Python that performs **face detection, emotion recognition, and color-based object detection** using a webcam.

This project demonstrates how **OpenCV and deep learning models** can be combined to build a simple intelligent monitoring system capable of analyzing live camera input.

---

## Features

* Real-time webcam video processing
* Face detection using **Haar Cascades (OpenCV)**
* Emotion recognition using **DeepFace**
* Red object detection using **HSV color segmentation**
* Live AI dashboard overlay
* Automatic logging of frames
* Emotion statistics saved to a file

---

## Tech Stack

* Python
* OpenCV
* NumPy
* DeepFace

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/vyanmadai7/ai-surveillance-dashboard.git
cd ai-surveillance-dashboard
```

### 2. Install dependencies

```bash
pip install opencv-python numpy deepface
```

---

## Run the Project

```bash
python main.py
```

Press **Q** to close the dashboard.

---

## Project Structure

```
ai-surveillance-dashboard
│
├── main.py
├── logs
│   ├── stats.txt
│   └── saved_frames
│
├── requirements.txt
└── README.md
```

---

## How It Works

1. The webcam captures live video frames.
2. OpenCV detects faces using Haar Cascade classifiers.
3. Each detected face is analyzed using **DeepFace** to determine the dominant emotion.
4. The system detects **red-colored objects** using HSV color masks.
5. All results are displayed in a **live AI dashboard overlay**.
6. Frames and statistics are saved automatically in the **logs** folder.

---

## Example Output

The dashboard displays:

* Number of detected faces
* Detected emotions
* Highlighted faces
* Detected red objects
* Real-time camera feed

Frames and logs are automatically stored with timestamps.

---

## Future Improvements

Possible upgrades for this project:

* YOLOv8 object detection
* Age and gender prediction
* Face recognition authentication system
* Web dashboard using FastAPI
* Cloud logging and analytics

---

## Author

**Vyan**
AI / ML Learner | Self taught Developer

GitHub:
https://github.com/vyanmadai7
