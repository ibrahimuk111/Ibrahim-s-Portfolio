# Homomorphic_Encryption_Inference_Engine

Homomorphic encryption inference pipeline allowing neural network evaluation directly over encrypted data (TenSEAL).

## Architecture

```
Homomorphic_Encryption_Inference_Engine/
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
docker build -t homomorphic_encryption_inference_engine .
docker run -p 8000:8000 homomorphic_encryption_inference_engine
```

## Features
- TenSEAL CKKS Scheme integration
- Zero-knowledge data inference
- Encrypted ciphertext predictions

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

