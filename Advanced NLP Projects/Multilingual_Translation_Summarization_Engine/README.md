# Multilingual_Translation_Summarization_Engine

Multilingual text translation and automated summarization pipeline using Hugging Face MarianMT and mBART transformers.

## System Architecture

```mermaid
graph TD
    Text[Input Multilingual Text] --> Summarizer[mBART / MarianMT Summarizer]
    Summarizer --> Translator[NLLB / M2M-100 Translation Model]
    Translator --> Output[Structured Multilingual Summary]

```

## Directory Structure

```
Multilingual_Translation_Summarization_Engine/
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

# Container build
docker build -t multilingual_translation_summarization_engine .
docker run -p 8000:8000 multilingual_translation_summarization_engine
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

