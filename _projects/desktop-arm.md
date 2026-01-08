---
title: "Desktop Arm"
excerpt: "Full-size 6-DOF 3D-printed robotic arm with ROS2 Humble, MoveIt2, Raspberry Pi 4, and Xbox teleoperation."
header:
  teaser: /assets/img/portfolio/arduino-chatgpt.PNG
  overlay_image: /assets/img/portfolio/arduino-chatgpt.PNG
  overlay_filter: 0.5
tags:
  - Robotics
  - ROS2
  - MoveIt2
  - Raspberry Pi
  - 3D Printing
github_url: https://github.com/Jshulgach/Desktop-Arm
order: 11
---

## Overview

The Desktop Arm is a complete ROS2-based robotic arm system featuring the BCN3D Moveo, a medium-sized fully 3D-printable 6-axis arm. Similar in aesthetics to industrial arms like the KUKA Agilus or Fanuc LR Mate, it's designed for personal use, research, and education at an affordable price.

## Key Features

- **Raspberry Pi 4 Model B** - Main processing unit for motion planning
- **Arduino Mega + RAMPS 1.4** - Motor control interface
- **ROS2 Humble** - Modern robotics middleware
- **MoveIt2** - Advanced motion planning and manipulation
- **All 3D Printable** - Only fasteners and motors needed
- **Under $1,000** - Complete B.O.M. available
- **DDNS Support** - Control over the internet

## System Architecture

```
┌──────────────────┐
│   Xbox Controller │
└────────┬─────────┘
         │ USB / Network
         ▼
┌──────────────────┐    ┌──────────────────┐
│  Raspberry Pi 4  │───▶│    Arduino Mega   │
│   ROS2 Humble    │    │   RAMPS 1.4       │
│   MoveIt2        │    │   Stepper Drivers │
└──────────────────┘    └────────┬─────────┘
                                 │
                                 ▼
                        ┌──────────────────┐
                        │   6-DOF Arm      │
                        │   (BCN3D Moveo)  │
                        └──────────────────┘
```

## Teleoperation Modes

### Local Control
```bash
ros2 launch desktop_arm teleop.launch.py
```

### Remote Control (Internet)
```bash
# On robot
ros2 launch desktop_arm teleop.launch.py start_server:=true manual:=false

# On client
python client-controller.py
```

## Available Commands

| Command | Description |
|---------|-------------|
| `enablemotor MOTOR` | Enable stepper driver |
| `movemotor MOTOR VALUE` | Move to position (deg) |
| `gripper VALUE` | Open (1) or close (0) |
| `robotinfo` | Print system status |
| `setmotorspeed MOTOR VALUE` | Adjust speed |

## Installation

1. Flash Ubuntu 22.04 LTS on Raspberry Pi 4
2. Clone repository to `~/ros2_ws/src`
3. Run `./install.sh` for ROS2, MoveIt2, dependencies
4. Flash Arduino firmware
5. Configure DDNS (optional)

## Demos

- **Dancing Demo** - Random joint movements showcase
- **Xbox Teleop** - Real-time joystick control
- **Simulated Model** - RViz2 visualization

## Links

- [GitHub Repository]({{ page.github_url }}){: .btn .btn--primary}
- [Build Guide (Instructables)](https://www.instructables.com/Build-a-Giant-3D-Printed-Robot-Arm/){: .btn .btn--info}
