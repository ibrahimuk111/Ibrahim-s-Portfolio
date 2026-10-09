"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Wine Quality Prediction - EDA & Classification
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import WineQualityPrediction_EDA_ClasEngine

def test_engine_execution():
    engine = WineQualityPrediction_EDA_ClasEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
