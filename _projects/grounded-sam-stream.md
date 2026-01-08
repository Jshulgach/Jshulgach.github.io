---
title: "Grounded SAM 2 Stream"
excerpt: "Early investigation into inferring user interest through natural language object detection using Grounding DINO, SAM 2, and LLMs."
header:
  teaser: /assets/img/portfolio/dino-stream.gif
  overlay_image: /assets/img/portfolio/dino-stream.gif
  overlay_filter: 0.5
tags:
  - Computer Vision
  - LLM
  - Object Detection
  - SAM
  - Deep Learning
order: 10
---

## Overview

**Grounded SAM 2 Stream** was an early investigation (2024) into inferring user interest from natural language queries. The system combines Grounding DINO for object detection with SAM 2 for segmentation and local LLMs via Ollama to interpret what the user wants to identify in a video stream.

## The Concept

Instead of requiring users to specify exact object classes, this system lets them describe what they're looking for in natural language:

> "I am looking for something blue that squirts water"

The LLM interprets this query and guides the vision models to find and track the relevant object in real-time.

## Key Features

- **Natural Language Queries** – Describe objects conversationally
- **Real-time Tracking** – Live video stream processing
- **Multi-Camera Support** – Stream from multiple webcams simultaneously
- **Local LLM Integration** – Uses Ollama for privacy-preserving inference

## Architecture

1. **Grounding DINO** – Open-vocabulary object detection
2. **SAM 2** – High-quality instance segmentation
3. **Ollama/LLM** – Natural language understanding and query interpretation
4. **Socket Server** – Receives queries from clients in real-time

## Historical Note

This project was an early prototype exploring how users might interact with vision systems more naturally. While the field has evolved significantly since 2024, it represented an interesting approach to bridging language and vision for assistive applications.

## Links

<a href="https://github.com/Jshulgach/Grounded-SAM-2-Stream" class="btn btn--primary"><i class="fab fa-github"></i> GitHub Repository</a>
