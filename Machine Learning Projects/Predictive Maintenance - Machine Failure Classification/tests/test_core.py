"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Predictive Maintenance - Machine Failure Classification
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import PredictiveMaintenance_MachineFEngine

def test_engine_execution():
    engine = PredictiveMaintenance_MachineFEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
