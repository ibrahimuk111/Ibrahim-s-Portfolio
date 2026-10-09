# FineTuned_Medical_Legal_Specialist_LLM

Domain-specialized LLM fine-tuning pipeline using Unsloth, QLoRA PEFT adapters, and automated GGUF quantization export.

## System Architecture

```mermaid
graph LR
    Dataset[Medical/Legal Domain Corpus] --> Tokenizer[Unsloth Fast Tokenizer]
    Tokenizer --> QLoRA[QLoRA 4-bit Adapter Training]
    QLoRA --> Merge[Adapter Merge & Quantization]
    Merge --> GGUF[GGUF Q4_K_M / Ollama Export]

```

## Directory Structure

```
FineTuned_Medical_Legal_Specialist_LLM/
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
docker build -t finetuned_medical_legal_specialist_llm .
docker run -p 8000:8000 finetuned_medical_legal_specialist_llm
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

