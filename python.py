import cv2
import numpy as np
from deepface import DeepFace
from datetime import datetime
import os

# create log folder
if not os.path.exists("logs"):
    os.makedirs("logs")

# load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not found")
    exit()

while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    annotated_frame = frame.copy()
    dominant_emotions = []

    for (x, y, w, h) in faces:

        cv2.rectangle(annotated_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_img = frame[y:y+h, x:x+w]

        try:
            result = DeepFace.analyze(
                face_img,
                actions=["emotion"],
                enforce_detection=False
            )

            emotion = result[0]["dominant_emotion"]
            dominant_emotions.append(emotion)

            cv2.putText(
                annotated_frame,
                emotion,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2,
            )

        except:
            cv2.putText(
                annotated_frame,
                "Unknown",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )

    # red color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 + mask2

    red_objects = cv2.bitwise_and(frame, frame, mask=red_mask)

    annotated_frame = cv2.addWeighted(annotated_frame, 1, red_objects, 0.5, 0)

    face_count = len(faces)

    cv2.putText(
        annotated_frame,
        f"Faces: {face_count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2,
    )

    emotion_summary = ", ".join(dominant_emotions) if dominant_emotions else "None"

    cv2.putText(
        annotated_frame,
        f"Emotions: {emotion_summary}",
        (10, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2,
    )

    cv2.imshow("Smart Dashboard", annotated_frame)

    # save logs
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    cv2.imwrite(f"logs/frame_{timestamp}.jpg", annotated_frame)

    with open("logs/stats.txt", "a") as f:
        f.write(f"{timestamp} Faces:{face_count}, Emotions:{emotion_summary}\n")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("Dashboard Closed")
