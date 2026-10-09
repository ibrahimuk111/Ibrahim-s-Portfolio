# Edge_Vision_Mobile_Scanner_App

Offline edge vision mobile scanner setup utilizing ONNX Mobile Runtime for sub-15ms real-time camera object detection and OCR.

## Architecture & System Flowchart

```mermaid
graph TD
    Camera[Mobile Camera Feed 60FPS] --> YOLOVision[ONNX Mobile NNAPI Engine]
    YOLOVision --> BBoxFilter[NMS Box Filter & OCR]
    BBoxFilter --> MobileAppUI[Flutter Mobile UI Display]

```

## Directory Structure

```
Edge_Vision_Mobile_Scanner_App/
├── src/           # Backend AI Core & Logic
├── lib/ / app/    # Mobile UI / Web Frontend
├── tests/         # Unit Test Suite
├── app.py         # FastAPI Gateway Application
├── Dockerfile     # Container Configuration
├── requirements.txt
└── LICENSE
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run backend API
python app.py

# Run tests
pytest tests/ -v

# Container deployment
docker build -t edge_vision_mobile_scanner_app .
docker run -p 8000:8000 edge_vision_mobile_scanner_app
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

