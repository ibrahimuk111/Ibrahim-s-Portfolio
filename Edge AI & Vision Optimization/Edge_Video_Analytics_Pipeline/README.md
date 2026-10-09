# Edge_Video_Analytics_Pipeline

Edge computer vision analytics pipeline for human action recognition, loitering alerts, and crowd counting.

## Architecture

```
Edge_Video_Analytics_Pipeline/
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
docker build -t edge_video_analytics_pipeline .
docker run -p 8000:8000 edge_video_analytics_pipeline
```

## Features
- Edge-optimized video processing
- Action recognition and counting
- Thermal and resource monitoring

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

