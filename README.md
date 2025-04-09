# Driver Drowsiness Detection System

This project uses computer vision to monitor a driver's face and detect signs of drowsiness based on eye closures over a series of frames. If drowsiness is detected, the system raises an alert with a visual cue and an audible alarm.

## Features
- Real-time face and eye detection using Haar Cascade Classifiers.
- Detects prolonged eye closure to identify possible drowsiness.
- Provides both visual and sound alerts to notify the driver.

## How It Works
1. **Face and Eye Detection**: The system uses OpenCV's pre-trained Haar Cascade Classifiers to detect a driver's face and eyes.
2. **Drowsiness Detection**: If the system detects no eyes in the frame for a predefined number of consecutive frames (`FRAME_THRESHOLD`), it determines the driver may be drowsy.
3. **Alert Mechanism**: A red alert message ("DROWSINESS ALERT!") is displayed on the screen, and a sound alarm is triggered using the winsound library.

## Requirements
- Python 3.x
- OpenCV
- Winsound (available by default on Windows)

## Installation
1. Clone the repository:
   ```bash
   git clone <https://github.com/ramkumark-dev/drowsy_analysis/edit/main>
2. Navigate to the project directory:

   ```bash
   cd <repository_directory>
3. Install dependencies:

   ```bash
   pip install opencv-python

##Usage
To start the system:

1. Ensure your webcam is functional and properly connected.

2. Run the Python script:

   ```bash
   python driver_drowsiness.py
3. When the program starts, your webcam feed will appear in a new window. The system will monitor your face and eyes for signs of drowsiness.

4. Press q on your keyboard to exit the program.

##Configuration
You can adjust the following constant in the script:

- FRAME_THRESHOLD: Number of consecutive frames with no detected eyes required to trigger the alarm. Increase this value for less sensitivity.

##Limitations
- Designed for single-driver detection; may not function optimally for multiple faces.
- Requires sufficient lighting for accurate detection.
- Sound alerts use the winsound library, which is Windows-specific.

##License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code.

