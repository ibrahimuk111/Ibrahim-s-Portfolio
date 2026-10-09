"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: LLM as a Judge - Automated Evaluation of Responses
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import LLMasaJudge_AutomatedEvaluatioEngine

def test_engine_execution():
    engine = LLMasaJudge_AutomatedEvaluatioEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
