# Enterprise_LLM_Guardrails_API

Production enterprise LLM guardrails REST API with PII scrubbing, toxicity checks, and prompt safety validation.

## Architecture

```
Enterprise_LLM_Guardrails_API/
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
docker build -t enterprise_llm_guardrails_api .
docker run -p 8000:8000 enterprise_llm_guardrails_api
```

## Features
- PII redaction
- Fast toxicity scoring
- Prompt injection and safety validation

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

