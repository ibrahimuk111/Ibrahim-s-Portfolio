# Multi_Camera_Object_Counting_App

Multi-camera real-time object tracking and virtual line-crossing occupancy analytics using YOLOv8 and DeepSORT.

## System Architecture

```mermaid
graph LR
    Cams[RTSP Camera Streams] --> YOLO[YOLOv8 Object Detector]
    YOLO --> DeepSORT[DeepSORT Multi-Target Tracker]
    DeepSORT --> ZoneGate[Virtual Line Crossing Logic]
    ZoneGate --> DashboardUI[Real-Time Occupancy Dashboard]

```

## Directory Structure

```
Multi_Camera_Object_Counting_App/
├── src/           # Core modules
├── tests/         # Unit tests (pytest)
├── app.py         # Application entry point
├── Dockerfile     # Container configuration
├── requirements.txt
└── LICENSE
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Run tests
pytest tests/ -v

# Container build
docker build -t multi_camera_object_counting_app .
docker run -p 8000:8000 multi_camera_object_counting_app
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

