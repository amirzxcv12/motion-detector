# Motion Detector

A beginner-friendly motion detection project made with Python and OpenCV.

## Features
- Live webcam input
- Background subtraction
- Moving-area rectangles
- Noise filtering
- Separate motion mask window

## Requirements
- Python 3
- A webcam

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# On Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
python motion_detector.py
```

Press **Q** to quit.

## How it works
OpenCV builds a model of the background and compares each new frame with it. Areas that change are treated as possible movement. Small areas are ignored to reduce noise.

## Project structure

```text
motion-detector/
├── motion_detector.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Creator
**Amir**

Made with Python and OpenCV 💜
