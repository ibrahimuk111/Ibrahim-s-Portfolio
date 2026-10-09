"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Financial_News_Sentiment_Classification_using_NLP_and_ML
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Financial_News_Sentiment_ClassEngine

def test_engine_execution():
    engine = Financial_News_Sentiment_ClassEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
