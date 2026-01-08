---
title: "TinyNML"
excerpt: "Embedded machine learning on microcontrollers for motion recognition, gesture control, and biosignal processing."
header:
  teaser: /assets/img/portfolio/tiny-nml.png
  overlay_image: /assets/img/portfolio/tiny-nml.png
  overlay_filter: 0.5
tags:
  - TinyML
  - Embedded Systems
  - Machine Learning
  - Raspberry Pi Pico
  - EMG
order: 4
---

## Overview

**TinyNML** is a growing collection of embedded machine learning projects developed in the Neuromechatronics Lab at Carnegie Mellon University. The repository focuses on deploying ML models on resource-constrained microcontrollers like the Raspberry Pi Pico and other edge devices.

Whether it's motion recognition, gesture control, biosignal processing, or edge AI inference pipelines, TinyNML provides a collaborative platform for prototyping and deploying models on embedded hardware.

## Current Projects

| Project | Description | Language | Hardware |
|---------|-------------|----------|----------|
| **pico_motion_classifier** | Real-time circular motion classification using MPU6050 | C++ | Pico W + MPU6050 + SSD1306 |
| **pico_emg_gesture_classifier** | EMG-based gesture classification | CircuitPython | Pico W + EMG electrodes |
| **pico_cnn_mnist_classifier** | CNN digit recognition with weight extraction (no TFLite) | CircuitPython | Pico + OV7670 camera |

## Project Goals

- Build scalable and modular TinyML applications on embedded hardware
- Combine mechatronics, biosignals, and ML inference for real-world applications
- Provide a collaborative platform for lab members to prototype and share models

## Links

<a href="https://github.com/Neuro-Mechatronics-Interfaces/TinyNML" class="btn btn--primary"><i class="fab fa-github"></i> GitHub Repository</a>
