"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Advanced_Mental_Health_Sentiment_Analysis_NLP_Project
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Advanced_Mental_Health_SentimeEngine

def test_engine_execution():
    engine = Advanced_Mental_Health_SentimeEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
