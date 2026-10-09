# Underwater_Visual_Enhancement_Detector

Color restoration, dehazing, and domain adaptation pipeline for marine object detection in low-visibility underwater environments.

## Architecture

```
Underwater_Visual_Enhancement_Detector/
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
docker build -t underwater_visual_enhancement_detector .
docker run -p 8000:8000 underwater_visual_enhancement_detector
```

## Features
- Underwater image dehazing
- Color balance correction
- Target identification in turbid water

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

