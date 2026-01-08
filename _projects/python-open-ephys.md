---
title: "Python Open-Ephys"
excerpt: "Python tools for streaming and processing EMG data from the Open-Ephys acquisition system."
header:
  teaser: /assets/img/portfolio/python-open-ephys.png
  overlay_image: /assets/img/portfolio/python-open-ephys.png
  overlay_filter: 0.5
tags:
  - Python
  - EMG
  - Data Acquisition
  - Open-Ephys
  - Neuroscience
order: 8
---

## Overview

**Python Open-Ephys** provides a set of tools for working with the Open-Ephys data acquisition system and GUI for electromyography (EMG) data. It enables real-time streaming and processing of neural/EMG signals through a simple Python interface.

## Features

- **Simple API**: Easy-to-use `OpenEphysClient` class for connecting to Open-Ephys GUI
- **Real-time Streaming**: Stream data via ZMQ plugin integration
- **LSL Support**: Lab Streaming Layer functionality for multi-device synchronization
- **Model Training**: Tools for training real-time decode models on EMG data

## Quick Example

```python
from open_ephys import OpenEphysClient

client = OpenEphysClient()
samples = client.get_samples(channel=8)
```

## Requirements

- Open-Ephys GUI with ZMQ Plugin
- Python 3.10+
- Works on Windows 11 (tested)

## Links

<a href="https://github.com/Neuro-Mechatronics-Interfaces/python-open-ephys" class="btn btn--primary"><i class="fab fa-github"></i> GitHub Repository</a>
