# Vector_Database_Benchmarking_Engine

Benchmarking suite evaluating retrieval latency, throughput, and memory footprint of FAISS, ChromaDB, and Pinecone.

## Architecture

```
Vector_Database_Benchmarking_Engine/
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
docker build -t vector_database_benchmarking_engine .
docker run -p 8000:8000 vector_database_benchmarking_engine
```

## Features
- FAISS vs ChromaDB vs Pinecone comparisons
- Latency QPS benchmarking
- Memory footprint estimation

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

