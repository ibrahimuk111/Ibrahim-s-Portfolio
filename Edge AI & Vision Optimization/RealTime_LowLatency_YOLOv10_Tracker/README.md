# RealTime_LowLatency_YOLOv10_Tracker

High-throughput, sub-10ms real-time object detection and tracking pipeline optimized with ONNX Runtime and TensorRT.

## Architecture

```
RealTime_LowLatency_YOLOv10_Tracker/
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

# Docker
docker build -t realtime_lowlatency_yolov10_tracker .
docker run -p 8000:8000 realtime_lowlatency_yolov10_tracker
```

## Features
- Real-time sub-10ms inference
- Object tracking with ByteTRACK/DeepSORT
- TensorRT and ONNX execution provider

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

