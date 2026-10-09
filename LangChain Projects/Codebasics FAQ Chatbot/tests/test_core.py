"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Codebasics FAQ Chatbot
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import CodebasicsFAQChatbotEngine

def test_engine_execution():
    engine = CodebasicsFAQChatbotEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
