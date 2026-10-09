"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Face Liveness Detection System
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import FaceLivenessDetectionSystemEngine

def test_engine_execution():
    engine = FaceLivenessDetectionSystemEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
