# Multi_RAG_Router_Agent

Multi-index LlamaIndex router agent dynamically routing user queries across specialized vector databases.

## System Architecture

```mermaid
graph TD
    Query[User Query] --> IntentRouter[LlamaIndex Selector / Router Agent]
    IntentRouter -->|Financial Keywords| FinIndex[(Financial Vector Index)]
    IntentRouter -->|Legal Keywords| LegalIndex[(Legal Vector Index)]
    IntentRouter -->|Tech Keywords| TechIndex[(Tech Documentation Index)]
    FinIndex --> Aggregator[Synthesized RAG Response]
    LegalIndex --> Aggregator
    TechIndex --> Aggregator

```

## Directory Structure

```
Multi_RAG_Router_Agent/
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
docker build -t multi_rag_router_agent .
docker run -p 8000:8000 multi_rag_router_agent
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

