"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer Shopping Trends & Basket Analysis
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import CustomerShoppingTrends_BasketAEngine

def test_engine_execution():
    engine = CustomerShoppingTrends_BasketAEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
