# AI Surveillance Dashboard

A simple **AI powered camera dashboard** built with Python....
It uses computer vision to detect **faces, emotions, and red objects** in real time from your webcam....

This project shows how basic **AI + computer vision** can be used to analyze live video and display useful information on screen....

---------------

## What This Project Does

When you run the program, it opens your webcam and creates a **live AI dashboard**....

The system can:------

* Detect **human faces**
* Recognize **basic emotions** (happy, sad, angry, etc.)
* Detect **red colored objects**
* Display everything in a **real-time dashboard**
* Save **frames and logs automatically**

This makes it a small example of how AI can be used in **surveillance, monitoring, or smart camera systems**....

-------------------

## Technologies Used

This project is built using:

* **Python** – main programming language
* **OpenCV** – for camera access and computer vision
* **NumPy** – for numerical operations
* **DeepFace** – for emotion detection using deep learning

-------------------

## How to Install

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/vyanmadai7/ai-surveillance-dashboard.git
cd ai-surveillance-dashboard
```

-------------------

### 2. Install Required Libraries

```bash
pip install opencv-python numpy deepface
```

-------------------

## How to Run the Project

Start the program with:

```bash
python python.py
```

Your webcam will open and the **AI dashboard will start running**.

Press **Q** on your keyboard to close the program.

-------------------

## Project Structure

```
ai-surveillance-dashboard
│
├── python.py         
├── logs/           
│   ├── stats.txt
│   └── frame_images
│
└── README.md
```

---------------

## How the System Works

1. The webcam captures video frames in real time.
2. OpenCV scans each frame to detect **faces**.
3. Each detected face is sent to **DeepFace**, which predicts the **dominant emotion**.
4. The program also detects **red colored objects** using HSV color filtering.
5. The results are drawn on the screen as a **live dashboard overlay**.
6. Frames and detection data are saved inside the **logs folder**.

-----------

## Example Output

The dashboard shows:

* Number of faces detected
* Emotion of each detected face
* Highlighted red objects
* Real-time camera feed
* Automatically saved logs

-----------

## Possible Future Improvements

This project can be expanded further, for example:

* Real **object detection with YOLO**
* **Age and gender detection**
* **Face recognition login system**
* A **web dashboard using FastAPI**
* Cloud storage for logs

-----------
