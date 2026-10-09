"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: AI_Powered_Flutter_Mobile_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.executorch_bridge import ExecuTorchBridge

def test_inference():
    b = ExecuTorchBridge()
    res = b.run_inference("Hello Mobile LLM")
    assert res["inference_time_ms"] > 0
    assert "ExecuTorch" in res["response"]
