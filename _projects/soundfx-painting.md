---
title: "SoundFX Painting"
excerpt: "Interactive art installation—a custom painting with Arduino-triggered sound effects to play cherished family memories."
header:
  teaser: /assets/img/portfolio/soundfx-painting.PNG
  overlay_image: /assets/img/portfolio/soundfx-painting.PNG
  overlay_filter: 0.5
tags:
  - Arduino
  - Hardware
  - Art
  - Audio
  - Gift
github_url: https://github.com/Jshulgach/SoundFX-Painting
order: 12
---

## Overview

The SoundFX Painting is an interactive art installation originally created as a Christmas gift for my mom. Behind a beautiful painting of our late family African Grey parrot lies a circuit that plays treasured sound recordings at the press of hidden buttons—bringing precious memories back to life.

## The Story

Our family bird had many memorable sayings that became part of daily life. Working with artist [Gabriella Kostadinova](https://www.gabrielakostadinova.com/), we created a portrait that not only captures the bird's likeness but also preserves its voice through carefully selected audio clips.

## Hardware Components

- **Adafruit Audio FX Board** - 16MB flash with WAV/OGG playback
- **LiPo Battery 2000mAh** - Portable power source
- **5V LiPo Power Boost** - Rechargeable power management
- **Mono Speaker 3W 4Ω** - Clear audio output
- **Tactile Buttons (3)** - Hidden triggers for sound bites
- **Volume Controls (2)** - Discrete volume adjustment
- **Toggle Switch** - Power on/off

## Wiring

The circuit can be mounted behind any painting or picture frame. A prototyping solder board reduces wiring complexity between modules.

```
┌─────────────────┐
│  Painting Frame │
├─────────────────┤
│ ┌─────────────┐ │
│ │  Audio FX   │ │◀── Trigger Pins (3 buttons)
│ │   Board     │ │◀── Volume Pins (2 buttons)
│ └──────┬──────┘ │
│        │        │
│ ┌──────▼──────┐ │
│ │  Speaker    │ │◀── Behind canvas
│ └─────────────┘ │
│                 │
│ ┌─────────────┐ │
│ │ LiPo + Boost│ │◀── Hidden compartment
│ └─────────────┘ │
└─────────────────┘
```

## Software (Optional)

While the Audio FX board works standalone via trigger pins, an Arduino sketch enables advanced control:

- **Serial Communication** - Command-based playback
- **Track Selection** - Play by number or filename
- **Volume Control** - Programmatic adjustment
- **Playlist Mode** - Sequential playback

## Making Your Own

1. **Choose a subject** - Pet, family member, favorite character
2. **Collect audio** - Record meaningful sounds/phrases
3. **Commission art** - Work with an artist or print a photo
4. **Build the circuit** - Follow the wiring diagram
5. **Hide components** - Mount behind the frame
6. **Enjoy memories** - Press buttons to bring back precious moments

## Links

- [GitHub Repository]({{ page.github_url }}){: .btn .btn--primary}
- [Audio FX Guide](https://learn.adafruit.com/adafruit-audio-fx-sound-board){: .btn .btn--info}
