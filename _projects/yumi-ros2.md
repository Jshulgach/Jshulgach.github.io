---
title: "YuMi ROS2"
excerpt: "ABB YuMi MoveIt2 configuration for ROS2 Jazzy—dual-arm motion planning, OMPL algorithms, and custom RViz setups."
header:
  teaser: /assets/img/portfolio/yumi-ros2.png
  overlay_image: /assets/img/portfolio/yumi-ros2.png
  overlay_filter: 0.5
tags:
  - ROS2
  - MoveIt2
  - Robotics
  - Motion Planning
  - ABB
github_url: https://github.com/Jshulgach/yumi_ros2
order: 9
---

## Overview

YuMi ROS2 provides a complete MoveIt2 configuration package for the ABB YuMi dual-arm collaborative robot, targeting ROS2 Jazzy. It enables sophisticated dual-arm motion planning, coordinated bimanual manipulation, and visualization in RViz with custom configurations.

## Key Features

- **Dual-Arm Planning** - Independent and synchronized motion planning for both arms
- **OMPL Integration** - Access to RRTConnect, PRM, BiTRRT, and other algorithms
- **KDL Kinematics** - Fast inverse kinematics using the KDL solver
- **Fake Controllers** - Simulate robot motion without physical hardware
- **Custom RViz Config** - Pre-configured visualization for YuMi's workspace

## Supported Planning Groups

| Group | Description |
|-------|-------------|
| `left_arm` | 7-DOF left arm planning |
| `right_arm` | 7-DOF right arm planning |
| `both_arms` | Coordinated dual-arm planning |
| `left_gripper` | SmartGripper finger control |
| `right_gripper` | SmartGripper finger control |

## Quick Start

```bash
# Clone to ROS2 workspace
cd ~/ros2_ws/src
git clone https://github.com/Jshulgach/yumi_ros2.git

# Install dependencies
rosdep install --from-paths src --ignore-src -r -y

# Build
colcon build --packages-select yumi_moveit_config

# Launch
ros2 launch yumi_moveit_config demo.launch.py
```

## Architecture

```
┌────────────────────┐
│   MoveIt2 Core     │
├────────────────────┤
│  OMPL Planner      │◀── Planning Algorithms
├────────────────────┤
│  KDL IK Solver     │◀── Inverse Kinematics
├────────────────────┤
│  Fake Controllers  │◀── Simulation Mode
└────────────────────┘
         │
         ▼
┌────────────────────┐
│     RViz2          │
│   Visualization    │
└────────────────────┘
```

## Applications

- **Research** - Bimanual manipulation experiments
- **Industrial Automation** - Assembly task planning
- **Education** - Learning dual-arm robotics concepts
- **Simulation** - Testing motion plans before deployment

## Links

- [GitHub Repository]({{ page.github_url }}){: .btn .btn--primary}
- [ROS2 Jazzy Docs](https://docs.ros.org/en/jazzy/){: .btn .btn--info}
