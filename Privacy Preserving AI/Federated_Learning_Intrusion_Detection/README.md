# Federated_Learning_Intrusion_Detection

Decentralized privacy-preserving Federated Learning system using Flower for CAN bus intrusion detection.

## Architecture

```
Federated_Learning_Intrusion_Detection/
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
docker build -t federated_learning_intrusion_detection .
docker run -p 8000:8000 federated_learning_intrusion_detection
```

## Features
- Flower Federated Server orchestration
- Secure parameter aggregation
- Decentralized intrusion classification

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

