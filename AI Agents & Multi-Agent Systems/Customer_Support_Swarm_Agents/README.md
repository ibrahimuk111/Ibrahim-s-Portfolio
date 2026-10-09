# Customer_Support_Swarm_Agents

A swarm-based customer support system with intelligent routing and specialized domain agents for billing, technical, shipping, and general queries.

## Architecture

```
Customer_Support_Swarm_Agents/
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
docker build -t customer_support_swarm_agents .
docker run -p 8000:8000 customer_support_swarm_agents
```

## Key Features
- **Router Agent**: Keyword-based intelligent query routing
- **Domain Specialists**: Billing, Technical, Shipping, General agents
- **Swarm Orchestration**: Unified controller with analytics
- **Escalation**: Automatic escalation for unresolvable queries

---

## Author & Licensing

**Author:** Muhammad Ibrahim
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.
