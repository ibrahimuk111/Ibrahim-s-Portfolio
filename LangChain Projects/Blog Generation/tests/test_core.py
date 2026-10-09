"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Blog Generation
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import BlogGenerationEngine

def test_engine_execution():
    engine = BlogGenerationEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
