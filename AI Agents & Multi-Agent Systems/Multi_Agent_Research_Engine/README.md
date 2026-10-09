# Multi_Agent_Research_Engine

A multi-agent research system using LangGraph/CrewAI patterns with Tavily search and Streamlit UI. Features Research, Synthesis, and Critic agents working in iterative loops.

## Architecture

```
Multi_Agent_Research_Engine/
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
docker build -t multi_agent_research_engine .
docker run -p 8000:8000 multi_agent_research_engine
```

## Key Features
- **Research Agent**: Autonomous web search via Tavily API
- **Synthesis Agent**: LLM-powered report generation
- **Critic Agent**: Quality scoring and iterative refinement
- **Graph Orchestration**: LangGraph-based agent workflow
- **Streamlit Dashboard**: Interactive research interface

---

## Author & Licensing

**Author:** Muhammad Ibrahim
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.
