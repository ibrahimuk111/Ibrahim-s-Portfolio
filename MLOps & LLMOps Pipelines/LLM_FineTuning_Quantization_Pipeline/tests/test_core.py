"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: LLM_FineTuning_Quantization_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.quantization import ModelQuantizer

def test_quantizer():
    q = ModelQuantizer()
    res = q.simulate_quantization("Llama-3-8B", "4bit")
    assert res["quantized_size_gb"] < res["original_size_gb"]
