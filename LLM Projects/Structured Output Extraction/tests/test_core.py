"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Structured Output Extraction
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import StructuredOutputExtractionEngine

def test_engine_execution():
    engine = StructuredOutputExtractionEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
