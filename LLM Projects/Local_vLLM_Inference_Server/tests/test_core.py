"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Local_vLLM_Inference_Server
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.vllm_engine import vLLMEngineServer

def test_vllm():
    v = vLLMEngineServer()
    res = v.generate_stream("Test prompt")
    assert res["throughput_tokens_per_sec"] > 100
