# RAG_Hallucination_Detector

Evaluation pipeline measuring context grounding, answer relevancy, and detecting hallucinated facts in RAG pipelines.

## Architecture

```
RAG_Hallucination_Detector/
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
docker build -t rag_hallucination_detector .
docker run -p 8000:8000 rag_hallucination_detector
```

## Features
- Faithfulness & Context grounding
- Answer Relevancy check
- Hallucination alerting dashboard

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

