# GraphRAG_KnowledgeGraph_Engine

Knowledge Graph Retrieval-Augmented Generation (GraphRAG) combining Neo4j graph entities, Cypher queries, and hybrid dense retrieval.

## System Architecture

```mermaid
graph TD
    Query[User Query] --> TripletExtractor[LangChain LLM Entity/Relation Extractor]
    TripletExtractor --> Neo4j[(Neo4j Graph DB Cypher Search)]
    Neo4j --> VectorStore[(FAISS / Subgraph Embedding)]
    VectorStore --> ContextBuilder[Hybrid Context Aggregator]
    ContextBuilder --> ResponseLLM[LLM Generator Response]

```

## Directory Structure

```
GraphRAG_KnowledgeGraph_Engine/
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
docker build -t graphrag_knowledgegraph_engine .
docker run -p 8000:8000 graphrag_knowledgegraph_engine
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

