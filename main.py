from ultralytics import YOLO
import cv2
import numpy as np

# Load YOLO model
model = YOLO("yolov8n.pt")

# RTSP URLs
camera_urls = [
    "rtsp://USERNAME:PASSWORD@CAMERA_IP:554/Streaming/Channels/102",
    "rtsp://USERNAME:PASSWORD@CAMERA_IP:554/Streaming/Channels/102",
    "rtsp://USERNAME:PASSWORD@CAMERA_IP:554/Streaming/Channels/102",
    "rtsp://USERNAME:PASSWORD@CAMERA_IP:554/Streaming/Channels/102"
]


# Open all cameras
caps = [cv2.VideoCapture(url) for url in camera_urls]

for i, cap in enumerate(caps):
    if not cap.isOpened():
        print(f"Cannot connect to Camera {i+1}")
        exit()

while True:

    frames = []

    for i, cap in enumerate(caps):

        ret, frame = cap.read()

        if not ret:
            frame = np.zeros((360, 640, 3), dtype=np.uint8)
            cv2.putText(frame,
                        f"Camera {i+1} Offline",
                        (120,180),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0,0,255),
                        2)

        else:
            results = model(frame)
            frame = results[0].plot()
            frame = cv2.resize(frame, (640, 360))

        frames.append(frame)

    # Create 2x2 grid
    top = np.hstack((frames[0], frames[1]))
    bottom = np.hstack((frames[2], frames[3]))
    combined = np.vstack((top, bottom))

    cv2.imshow("YOLO - 4 Cameras", combined)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

for cap in caps:
    cap.release()

cv2.destroyAllWindows()