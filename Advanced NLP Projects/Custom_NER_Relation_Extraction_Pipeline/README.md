# Custom_NER_Relation_Extraction_Pipeline

Custom Named Entity Recognition (NER) and binary relation extraction pipeline using PyTorch and spaCy architecture.

## System Architecture

```mermaid
graph LR
    Input[Raw Unstructured Text] --> Tok[spaCy / Transformer Tokenizer]
    Tok --> NER[Named Entity Recognition Model]
    NER --> RelExtractor[Relation Extraction Model]
    RelExtractor --> Graph[(Structured Entity-Relation Graph)]

```

## Directory Structure

```
Custom_NER_Relation_Extraction_Pipeline/
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
docker build -t custom_ner_relation_extraction_pipeline .
docker run -p 8000:8000 custom_ner_relation_extraction_pipeline
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

