# Multi_Modal_Assistant_Agent

A multi-modal AI assistant that processes text, images, and voice inputs through a unified LangChain agent interface.

## Architecture

```
Multi_Modal_Assistant_Agent/
+-- src/           # Core modules
+-- tests/         # Unit tests (pytest)
+-- app.py         # Application entry point
+-- Dockerfile     # Container configuration
+-- requirements.txt
+-- LICENSE
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
docker build -t multi_modal_assistant_agent .
docker run -p 8000:8000 multi_modal_assistant_agent
```

## Key Features
- **Text Processing**: Conversational AI with memory
- **Vision Analysis**: Image understanding via GPT-4o
- **Voice Input**: Whisper-based transcription
- **Unified Agent**: Single orchestrator for all modalities

---

## Author & Licensing

**Author:** Muhammad Ibrahim
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.
