"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Image Captioning
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import ImageCaptioningEngine

def test_engine_execution():
    engine = ImageCaptioningEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
