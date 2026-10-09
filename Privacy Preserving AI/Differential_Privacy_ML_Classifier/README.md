# Differential_Privacy_ML_Classifier

Privacy-preserving machine learning model trained with PyTorch & Opacus for mathematical privacy guarantees.

## Architecture

```
Differential_Privacy_ML_Classifier/
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
docker build -t differential_privacy_ml_classifier .
docker run -p 8000:8000 differential_privacy_ml_classifier
```

## Features
- Epsilon-Delta privacy budgeting
- Clipped gradient noise injection
- Tradeoff curve analysis

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

