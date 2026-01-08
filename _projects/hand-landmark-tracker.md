---
title: "Hand Landmark Tracker"
excerpt: "MediaPipe-based hand tracking with Kalman filtering, LSL streaming, EMG-to-joint-angle regression, and robot control demos."
header:
  teaser: /assets/img/portfolio/Hands.png
  overlay_image: /assets/img/portfolio/Hands.png
  overlay_filter: 0.5
tags:
  - Computer Vision
  - Python
  - MediaPipe
  - Robotics
  - EMG
github_url: https://github.com/Jshulgach/Hand-Landmark-Tracker
order: 5
---

## Overview

Hand Landmark Tracker is a Python package that leverages Google's MediaPipe to detect and track 21 hand landmarks in real-time from webcam or video input. Beyond basic tracking, it includes Kalman filtering for smooth trajectories, Lab Streaming Layer (LSL) support for multi-device synchronization, and example integrations with robotic arms.

## Key Features

- **21 Landmark Detection** - Fingertips, knuckles, wrist points via MediaPipe
- **Kalman Filtering** - Temporal smoothing to reduce jitter
- **LSL Streaming** - Broadcast hand pose data for external applications
- **EMG-to-Joint Regression** - Predict hand joint angles from EMG signals
- **Robot Control Demos** - Control Mini-Arm and InMoov robots with hand gestures
- **Virtual Hand Rendering** - 3D visualization of tracked hand skeleton

## Applications

- **Gesture Recognition** - Classify hand poses for UI control
- **Teleoperation** - Control robotic hands in real-time
- **Rehabilitation** - Track patient hand movements during therapy
- **VR/AR Interaction** - Natural hand input for immersive environments

## Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌────────────────┐
│  Webcam Input   │───▶│  MediaPipe   │───▶│ Kalman Filter  │
└─────────────────┘    │  Hand Model  │    └───────┬────────┘
                       └──────────────┘            │
                                                   ▼
┌─────────────────┐    ┌──────────────┐    ┌────────────────┐
│  Robot Control  │◀───│  LSL Stream  │◀───│ 21 Landmarks   │
└─────────────────┘    └──────────────┘    └────────────────┘
```

## Example: Robot Teleoperation

```python
from hand_tracker import HandTracker
from mini_arm import MiniArmClient

tracker = HandTracker(stream_lsl=True)
robot = MiniArmClient(port='COM3')

for landmarks in tracker.run():
    # Map index finger position to robot end-effector
    target = landmarks['INDEX_FINGER_TIP']
    robot.send(f'set_pose:{target.tolist()}')
```

## Links

- [GitHub Repository]({{ page.github_url }}){: .btn .btn--primary}
- [Demo Video](https://youtube.com){: .btn .btn--info}
