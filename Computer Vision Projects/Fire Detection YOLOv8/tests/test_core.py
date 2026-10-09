"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Fire Detection YOLOv8
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import FireDetectionYOLOv8Engine

def test_engine_execution():
    engine = FireDetectionYOLOv8Engine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
