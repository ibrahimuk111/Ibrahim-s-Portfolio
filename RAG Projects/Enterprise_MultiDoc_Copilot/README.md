# Enterprise_MultiDoc_Copilot

Enterprise multi-document analysis copilot with PDF/Excel parsing, parent-child chunking, cross-encoder re-ranking, and page citation tracking.

## System Architecture

```mermaid
graph LR
    Docs[PDF / Excel Files] --> Parser[Unstructured Multi-Modal Parser]
    Parser --> Chunking[Parent-Child Semantic Chunking]
    Chunking --> FAISS[(FAISS Vector Store)]
    FAISS --> RERANK[Cross-Encoder Re-Ranker]
    RERANK --> Copilot[Copilot Generator with Page Citations]

```

## Directory Structure

```
Enterprise_MultiDoc_Copilot/
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
docker build -t enterprise_multidoc_copilot .
docker run -p 8000:8000 enterprise_multidoc_copilot
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

