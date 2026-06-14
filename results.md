# Results

## System Performance

The AI Fire Assistant System successfully detects fire in real-time using a YOLOv5-based object detection model. The system processes live video from a webcam and identifies the presence and location of fire within the frame.

## Hardware Integration

The detected fire position is transmitted to an Arduino through serial communication. Based on the detected location, the servo motor adjusts its position to target the fire, while the water pump is activated to simulate an automated fire suppression response.

## Detection Accuracy

The trained fire detection model achieved approximately 85% detection accuracy during testing. The system was able to detect fire under different lighting conditions and backgrounds while maintaining real-time performance.

## Key Outcomes

* Real-time fire detection using computer vision.
* Automated communication between Python and Arduino.
* Servo motor movement based on fire location.
* Automatic activation of water pump upon fire detection.
* Successful integration of software and hardware components.

## Conclusion

The project demonstrates the feasibility of combining artificial intelligence and embedded systems for automated fire detection and response. The developed prototype provides a foundation for future improvements such as IoT connectivity, mobile alerts, and deployment on edge devices.
