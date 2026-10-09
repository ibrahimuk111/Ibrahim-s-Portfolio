"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer Churn Prediction & Exploratory Analysis
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import CustomerChurnPrediction_ExplorEngine

def test_engine_execution():
    engine = CustomerChurnPrediction_ExplorEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
