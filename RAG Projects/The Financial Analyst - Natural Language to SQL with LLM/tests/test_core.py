"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: The Financial Analyst - Natural Language to SQL with LLM
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import TheFinancialAnalyst_NaturalLanEngine

def test_engine_execution():
    engine = TheFinancialAnalyst_NaturalLanEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
