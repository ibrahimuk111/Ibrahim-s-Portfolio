# End_To_End_CI_CD_ML_Pipeline

Production end-to-end CI/CD machine learning pipeline with Docker, PyTest, GitHub Actions integration, and FastAPI endpoints.

## Architecture

```
End_To_End_CI_CD_ML_Pipeline/
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
docker build -t end_to_end_ci_cd_ml_pipeline .
docker run -p 8000:8000 end_to_end_ci_cd_ml_pipeline
```

## Features
- Automated GitHub Actions workflow trigger
- PyTest verification gate
- Dockerized API deployment

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

