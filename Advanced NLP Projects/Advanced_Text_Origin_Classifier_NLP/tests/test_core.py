"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Advanced_Text_Origin_Classifier_NLP
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Advanced_Text_Origin_ClassifieEngine

def test_engine_execution():
    engine = Advanced_Text_Origin_ClassifieEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
