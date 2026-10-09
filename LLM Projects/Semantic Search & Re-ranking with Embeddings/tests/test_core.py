"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Semantic Search & Re-ranking with Embeddings
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import SemanticSearch_Re_rankingwithEEngine

def test_engine_execution():
    engine = SemanticSearch_Re_rankingwithEEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
