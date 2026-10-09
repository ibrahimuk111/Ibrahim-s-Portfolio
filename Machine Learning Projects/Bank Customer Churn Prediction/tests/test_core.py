"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Bank Customer Churn Prediction
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import BankCustomerChurnPredictionEngine

def test_engine_execution():
    engine = BankCustomerChurnPredictionEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
