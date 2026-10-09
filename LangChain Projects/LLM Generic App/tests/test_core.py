"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: LLM Generic App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import LLMGenericAppEngine

def test_engine_execution():
    engine = LLMGenericAppEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
