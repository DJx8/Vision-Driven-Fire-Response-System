# Vision-Driven-Fire-Response-System

## Overview

The AI Fire Assistant System is a computer vision-based fire detection and response system developed using YOLOv5, Python, OpenCV, and Arduino. The system detects fire in real-time through a webcam feed and automatically activates a hardware-based response mechanism.

When fire is detected, the system determines the position of the fire within the camera frame and sends the information to an Arduino. The Arduino controls a servo motor and water pump to direct the suppression mechanism toward the detected fire location.

---

## Features

* Real-time fire detection using YOLOv5
* Live webcam monitoring
* Arduino and Python serial communication
* Servo motor-based targeting system
* Automatic water pump activation
* Visual fire detection with bounding boxes
* Automated fire response mechanism

---

## Technologies Used

### Software

* Python
* YOLOv5
* OpenCV
* PyTorch
* NumPy
* PySerial

### Hardware

* Arduino Uno
* SG90 Servo Motor
* Mini Water Pump
* L298 Motor Driver
* USB Camera/Webcam
* 18650 Lithium-Ion Batteries

---

## System Workflow

1. The webcam continuously captures video frames.
2. The YOLOv5 model analyzes each frame for fire.
3. If fire is detected, the fire location is determined.
4. The fire coordinates are sent to the Arduino through serial communication.
5. The servo motor adjusts its position toward the detected fire.
6. The water pump is activated to simulate fire suppression.
7. When no fire is detected, the system returns to its standby state.

---

## Project Structure

```text
AI-Fire-Assistant-System/
│
├── src/
│   └── fire_detection_system.py
│
├── arduino/
│   └── fire_assistant.ino
│
├── models/
│   └── fire1.pt
│
├── images/
├── docs/
├── results/
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Fire-Assistant-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### YOLOv5 Dependency

This project uses components from the YOLOv5 framework.

Clone the YOLOv5 repository and install its requirements before running the project:

```bash
git clone https://github.com/ultralytics/yolov5.git
```

---

## Running the Project

Connect the Arduino and upload the Arduino sketch.

Update the serial port in the Python script if necessary:

```python
arduino = serial.Serial('COM5', 9600, timeout=1)
```

Run:

```bash
python fire_detection_system.py
```

Press **Q** to exit the application.

---

## Results

The system successfully demonstrates:

* Real-time fire detection
* Fire position tracking
* Arduino communication
* Servo motor control
* Automatic pump activation

The fire detection model achieved approximately 85% detection accuracy during testing.

---

## Future Improvements

* Smoke detection support
* Mobile notification system
* Raspberry Pi deployment
* IoT-based remote monitoring
* Improved detection under challenging lighting conditions

---

## Author

Dhananjay A.V

---

