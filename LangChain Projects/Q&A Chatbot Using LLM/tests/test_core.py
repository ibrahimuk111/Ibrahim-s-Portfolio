"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Q&A Chatbot Using LLM
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Q_AChatbotUsingLLMEngine

def test_engine_execution():
    engine = Q_AChatbotUsingLLMEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
