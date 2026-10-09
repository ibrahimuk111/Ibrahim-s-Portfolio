"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Web Page Summarization
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import WebPageSummarizationEngine

def test_engine_execution():
    engine = WebPageSummarizationEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
