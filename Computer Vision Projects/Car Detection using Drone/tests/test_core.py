"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Car Detection using Drone
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import CarDetectionusingDroneEngine

def test_engine_execution():
    engine = CarDetectionusingDroneEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
