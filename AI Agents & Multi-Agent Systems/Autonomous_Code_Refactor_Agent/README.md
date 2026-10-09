# Autonomous_Code_Refactor_Agent

An autonomous code refactoring agent using AST analysis and LLM-based suggestions. Detects code smells, suggests improvements, and generates refactored code.

## Architecture

```
Autonomous_Code_Refactor_Agent/
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
docker build -t autonomous_code_refactor_agent .
docker run -p 8000:8000 autonomous_code_refactor_agent
```

## Key Features
- **AST Analysis**: Deep Python code structure analysis
- **Code Smell Detection**: Identifies long functions, deep nesting, missing docstrings
- **Refactoring Engine**: Generates actionable improvement suggestions
- **Confidence Scoring**: Ranks suggestions by reliability

---

## Author & Licensing

**Author:** Muhammad Ibrahim
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.
