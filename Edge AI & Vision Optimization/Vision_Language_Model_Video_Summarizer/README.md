# Vision_Language_Model_Video_Summarizer

VLM-driven video log analyzer and event summarizer using multimodal LLMs (LLaVA / Qwen2-VL).

## Architecture

```
Vision_Language_Model_Video_Summarizer/
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
docker build -t vision_language_model_video_summarizer .
docker run -p 8000:8000 vision_language_model_video_summarizer
```

## Features
- Frame-by-frame multimodal narration
- Automated event timestamping
- Natural language video log search

---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

