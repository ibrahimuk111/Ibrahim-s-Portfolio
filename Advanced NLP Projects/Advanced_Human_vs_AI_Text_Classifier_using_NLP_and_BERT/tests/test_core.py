"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Advanced_Human_vs_AI_Text_ClasEngine

def test_engine_execution():
    engine = Advanced_Human_vs_AI_Text_ClasEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
