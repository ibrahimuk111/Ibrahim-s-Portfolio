"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Self Driving Car
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import SelfDrivingCarEngine

def test_engine_execution():
    engine = SelfDrivingCarEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
