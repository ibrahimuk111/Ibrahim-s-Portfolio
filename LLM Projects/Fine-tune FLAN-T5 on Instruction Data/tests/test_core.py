"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Fine-tune FLAN-T5 on Instruction Data
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Fine_tuneFLAN_T5onInstructionDEngine

def test_engine_execution():
    engine = Fine_tuneFLAN_T5onInstructionDEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
