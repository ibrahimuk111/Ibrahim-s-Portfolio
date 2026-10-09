"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Self-Ask with Web Search
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Self_AskwithWebSearchEngine

def test_engine_execution():
    engine = Self_AskwithWebSearchEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
