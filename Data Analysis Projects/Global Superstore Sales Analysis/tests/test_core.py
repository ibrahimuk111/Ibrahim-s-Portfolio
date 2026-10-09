"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Global Superstore Sales Analysis
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import GlobalSuperstoreSalesAnalysisEngine

def test_engine_execution():
    engine = GlobalSuperstoreSalesAnalysisEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
