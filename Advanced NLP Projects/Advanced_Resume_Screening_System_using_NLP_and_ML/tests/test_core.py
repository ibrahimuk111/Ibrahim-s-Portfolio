"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Advanced_Resume_Screening_System_using_NLP_and_ML
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Advanced_Resume_Screening_SystEngine

def test_engine_execution():
    engine = Advanced_Resume_Screening_SystEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
