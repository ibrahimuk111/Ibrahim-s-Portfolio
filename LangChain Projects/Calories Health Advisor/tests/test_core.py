"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Calories Health Advisor
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import CaloriesHealthAdvisorEngine

def test_engine_execution():
    engine = CaloriesHealthAdvisorEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
