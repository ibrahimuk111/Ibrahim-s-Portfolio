"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Conversational Memory with Summarization
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import ConversationalMemorywithSummarEngine

def test_engine_execution():
    engine = ConversationalMemorywithSummarEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
