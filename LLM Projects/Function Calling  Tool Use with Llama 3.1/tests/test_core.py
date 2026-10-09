"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Function Calling  Tool Use with Llama 3.1
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import FunctionCallingToolUsewithLlamEngine

def test_engine_execution():
    engine = FunctionCallingToolUsewithLlamEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
