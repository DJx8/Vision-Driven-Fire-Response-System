import sys
import os
from pathlib import Path
import cv2
import serial
import time
import torch
import numpy as np
from models.common import DetectMultiBackend
from utils.general import non_max_suppression, scale_boxes

# Add the current folder to the system path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Setup serial communication with Arduino
try:
    arduino = serial.Serial('COM5', 9600, timeout=1)
    time.sleep(2)  # Reduced delay
    print("✅ Connected to Arduino on COM5")
except Exception as e:
    print(f"❌ Error: Could not connect to Arduino. {e}")
    arduino = None

# Load YOLOv5 model
device = torch.device('cpu')  # Use 'cuda' if available
model = DetectMultiBackend("fire1.pt", device=device)
model.model.eval()

# Open webcam (Built-in = 0, External = 1)
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ No working webcam found!")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Could not read frame!")
        break

    # Convert frame for YOLO processing
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (640, 640))
    img = torch.from_numpy(img).permute(2, 0, 1).float() / 255.0
    img = img.unsqueeze(0).to(device)

    # Run YOLO fire detection
    with torch.no_grad():
        pred = model(img, augment=False)
        results = non_max_suppression(pred, conf_thres=0.4, iou_thres=0.35)

    fire_detected = False
    fire_x_center = None

    for result in results:
        if result is not None and len(result):
            for *xyxy, conf, cls in result:
                if int(cls) == 0:  # Fire detected
                    fire_detected = True
                    x1, y1, x2, y2 = map(int, xyxy)
                    fire_x_center = (x1 + x2) // 2  # Get center of fire
                    
                    # Draw bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                    cv2.putText(frame, f"Fire {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                    print(f"🔥 Fire detected at X={fire_x_center}, sending to Arduino")
                    break  # Take only the first detected fire

    if fire_detected:
        fire_data = f"FIRE {fire_x_center}\n"
        if arduino:
            arduino.write(fire_data.encode())  # Send fire position
            time.sleep(0.01)  # Reduced delay
    else:
        if arduino:
            arduino.write(b"NO_FIRE\n")  # Stop pump & reset servo
            print("✅ No fire detected. Signal sent to Arduino")

    # Show video feed with bounding boxes
    cv2.imshow("Fire Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
if arduino:
    arduino.close()
