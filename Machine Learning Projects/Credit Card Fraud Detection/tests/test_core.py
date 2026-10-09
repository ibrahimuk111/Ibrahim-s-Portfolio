"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Credit Card Fraud Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import CreditCardFraudDetectionEngine

def test_engine_execution():
    engine = CreditCardFraudDetectionEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
