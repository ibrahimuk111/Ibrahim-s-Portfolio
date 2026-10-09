# VLM_Video_QA_Summarizer

Vision-Language Model video scene QA and temporal action summarization utilizing Qwen2-VL multimodal embeddings.

## System Architecture

```mermaid
graph TD
    Video[Video Stream] --> FrameExtractor[Uniform Keyframe Extractor]
    FrameExtractor --> VLM[Qwen2-VL Vision-Language Encoder]
    VLM --> TemporalAttention[Temporal Cross-Attention Layer]
    TemporalAttention --> ResponseGenerator[Video QA Answer Generator]

```

## Directory Structure

```
VLM_Video_QA_Summarizer/
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
docker build -t vlm_video_qa_summarizer .
docker run -p 8000:8000 vlm_video_qa_summarizer
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

