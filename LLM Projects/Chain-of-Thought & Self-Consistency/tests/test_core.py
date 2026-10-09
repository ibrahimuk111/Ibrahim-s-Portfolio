"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Chain-of-Thought & Self-Consistency
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Chain_of_Thought_Self_ConsisteEngine

def test_engine_execution():
    engine = Chain_of_Thought_Self_ConsisteEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
