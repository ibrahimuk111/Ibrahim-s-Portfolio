"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Text-to-SQL with Llama
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Text_to_SQLwithLlamaEngine

def test_engine_execution():
    engine = Text_to_SQLwithLlamaEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
