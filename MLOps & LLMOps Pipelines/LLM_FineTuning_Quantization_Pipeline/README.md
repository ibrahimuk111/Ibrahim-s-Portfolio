# LLM_FineTuning_Quantization_Pipeline

Automated fine-tuning, QLoRA adapter extraction, and GGUF/AWQ model quantization pipeline.

## Architecture

```
LLM_FineTuning_Quantization_Pipeline/
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
docker build -t llm_finetuning_quantization_pipeline .
docker run -p 8000:8000 llm_finetuning_quantization_pipeline
```

## Features
- QLoRA fine-tuning config generation
- 4-bit / 8-bit quantization benchmarking
- vLLM deployment specs generator

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

