# Real-Time AI Video Analytics

A real-time AI-powered video analytics system that processes live RTSP camera streams and performs object detection using YOLOv8 and OpenCV.

The project demonstrates how traditional CCTV infrastructure can be enhanced with Computer Vision to provide intelligent, centralized video monitoring.

---

## 🚀 Project Overview

Traditional CCTV systems are mainly used for monitoring and recording.

This project explores how AI and Computer Vision can transform live camera feeds into an intelligent video analytics system.

The application:

- Connects to live IP cameras through RTSP
- Processes multiple camera streams simultaneously
- Performs real-time object detection using YOLOv8
- Displays detected objects with bounding boxes and confidence scores
- Combines multiple camera feeds into a unified monitoring dashboard
- Handles camera connection failures by displaying an offline status

---

## 🧠 Technologies Used

- **Python**
- **YOLOv8**
- **Ultralytics**
- **OpenCV**
- **NumPy**
- **RTSP**
- **IP Cameras**
- **Computer Vision**

---

## 🏗️ System Architecture

```text
             IP Cameras
                  │
                  │ RTSP Streams
                  ▼
        ┌─────────────────────┐
        │   OpenCV Capture    │
        │   Video Streams     │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │      YOLOv8         │
        │  Object Detection   │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Detection Results   │
        │                     │
        │ • Objects           │
        │ • Bounding Boxes    │
        │ • Confidence Scores │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │ Unified Monitoring  │
        │      Dashboard      │
        └─────────────────────┘

