---
title: "Mini-Arm"
excerpt: "Miniature 6-DOF 3D-printed robot arm with CircuitPython firmware, internal IK solver, and ROS2 integration—under $100."
header:
  teaser: /assets/img/portfolio/robotic-arm-3d-model-2023.png
  overlay_image: /assets/img/portfolio/robotic-arm-3d-model-2023.png
  overlay_filter: 0.5
tags:
  - Robotics
  - CircuitPython
  - ROS2
  - 3D Printing
  - Inverse Kinematics
github_url: https://github.com/Jshulgach/Mini-Arm
order: 3
---

## Overview

The Mini-Arm is a portable, miniature 6-DOF robotic arm that's 95% 3D-printable and costs under $100 to build. Running on a Raspberry Pi Pico microcontroller with CircuitPython, it features an internal inverse kinematics solver—no external computer needed for basic operation!

## Key Features

- **Raspberry Pi Pico 2** - Cost-effective microcontroller with CircuitPython
- **Internal IK Solver** - Handles joint calculations on-device using NumPy
- **95% 3D Printable** - Only fasteners and servos needed
- **Total Cost ≤ $100** - Accessible for education and hobbyists
- **Lightweight** - Weighs less than 1 lb (~0.3 kg)
- **Python API** - `MiniArmClient` class for serial communication
- **ROS2 Integration** - MoveIt2 and RViz2 visualization packages

## Available Commands

```
movemotor  MOTOR VALUE   | Move motor to absolute position (deg)
set_pose   [X,Y,Z,R,P,Y] | Cartesian end-effector control
get_pose                 | Read current position & orientation
set_gripper STATE        | Open/close gripper
home                     | Return to home position
trajectory PATTERN       | Execute predefined trajectories
```

## Quick Start

```python
from mini_arm import MiniArmClient

# Connect to Mini-Arm
client = MiniArmClient(port='COM3', baudrate=9600, verbose=True)

# Send commands
client.send('home')
client.send('set_pose:[0.135,0.0,0.22]')
client.send('set_gripper:close')

client.disconnect()
```

## Project Structure

```
Mini-Arm/
├── mini_arm.py          # Python client library
├── pico/                # CircuitPython firmware
├── examples/
│   ├── 01_basic_control/
│   ├── 02_trajectory/
│   ├── 02_xbox_teleop/  # Xbox controller control
│   └── 03_analysis/     # Motion capture comparison
├── miniarm_ros/         # ROS2 packages
└── assets/              # Images, docs
```

## Demos

- **Xbox Teleop** - Real-time joystick control
- **Trajectory Execution** - Circular and custom paths
- **Motion Analysis** - Compare commanded vs actual trajectories

## Links

- [GitHub Repository]({{ page.github_url }}){: .btn .btn--primary}
- [Build Guide](https://howtomechatronics.com/tutorials/arduino/diy-arduino-robot-arm-with-smartphone-control/){: .btn .btn--info}
