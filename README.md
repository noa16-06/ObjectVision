# YOLO Object Detector

This Python script uses **YOLOv8** and **OpenCV** to detect objects in real-time via your webcam. Detected objects are highlighted with colored rectangles, showing their class names and confidence scores.

## Features

- Real-time object detection using your webcam
- Custom colors for:
  - Person (Green)
  - Cell Phone (Blue)
  - Laptop (Red)
- Default yellow color for all other objects
- Displays rectangles, object centers, and labels on detected objects

## Requirements

- Python 3.8 or higher
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- OpenCV

### Install Dependencies

```bash
pip install ultralytics opencv-python
```

### Usage

Clone the repo

The YOLOv8 Nano model (yolov8n.pt) is used by default. You can also use other YOLOv8 models.

Run the script:
```bash
python main.py
```
A webcam window will open. Press q to quit.
