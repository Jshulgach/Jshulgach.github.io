---
title: "MicroLLM"
excerpt: "World's first real-time voice assistant on Raspberry Pi Pico W—Groq LLaMA inference with ElevenLabs TTS via I2S audio."
header:
  teaser: /assets/img/portfolio/llama-cameras.png
  overlay_image: /assets/img/portfolio/llama-cameras.png
  overlay_filter: 0.5
tags:
  - LLM
  - Embedded Systems
  - CircuitPython
  - Voice AI
  - IoT
github_url: https://github.com/Jshulgach/MicroLLM
order: 7
---

## Overview

MicroLLM is the world's first real-time voice assistant that runs entirely on a Raspberry Pi Pico W! By leveraging Groq's blazing-fast LLaMA API and ElevenLabs for natural-sounding text-to-speech, it delivers contextual AI responses through a DAC via I2S audio output—all on a $6 microcontroller.

## ✨ Features

- 🤖 **Contextual LLM Responses** - Powered by Groq's LLaMA 3 API
- 🔊 **Real-Time TTS** - Natural speech via ElevenLabs PCM 24kHz stream
- 📶 **Wi-Fi Connectivity** - True IoT integration with CircuitPython
- 🧠 **Fully Embedded** - No PC or Raspberry Pi OS required!

## Hardware Requirements

- Raspberry Pi Pico W
- MAX98357A I2S DAC
- 4-to-8 Ohm Speaker
- 5V USB Power

## Wiring

| Pico Pin | MAX98357A Pin |
|----------|---------------|
| GP1 | BCLK |
| GP0 | LRCK |
| GP9 | DIN |
| GND | GND |
| 3V3 | VDD |

## Setup

1. **Flash CircuitPython** - Use the provided `.uf2` firmware
2. **Copy Files** - Transfer `code.py` and `lib/` folder to Pico
3. **Configure API Keys** - Edit `settings.toml`:

```toml
CIRCUITPY_WIFI_SSID = "YourWiFiNetwork"
CIRCUITPY_WIFI_PASSWORD = "YourPassword"
ELEVENLABS_API_KEY = "your-elevenlabs-api-key"
GROQ_API_KEY = "your-groq-api-key"
```

4. **Power On** - The Pico connects to WiFi and starts listening!

## How It Works

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Pico W    │───▶│  Groq API   │───▶│ LLaMA 3 LLM │
│   (WiFi)    │    │  (Cloud)    │    │             │
└─────────────┘    └─────────────┘    └──────┬──────┘
                                             │
                          Text Response      │
                                             ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Speaker   │◀───│  I2S DAC    │◀───│ ElevenLabs  │
│             │    │ (MAX98357A) │    │ TTS Stream  │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Example: Groq Query

```python
import adafruit_requests

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    json={"model": "llama3-8b-8192", "messages": messages},
    headers={"Authorization": f"Bearer {groq_api_key}"}
)

answer = response.json()["choices"][0]["message"]["content"]
print("Response:", answer)
```

## Links

- [GitHub Repository]({{ page.github_url }}){: .btn .btn--primary}
- [Groq Cloud](https://groq.com/){: .btn .btn--info}
- [ElevenLabs](https://elevenlabs.io/){: .btn .btn--info}
