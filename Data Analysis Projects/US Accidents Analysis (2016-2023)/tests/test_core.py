"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: US Accidents Analysis (2016-2023)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import USAccidentsAnalysis(2016_2023)Engine

def test_engine_execution():
    engine = USAccidentsAnalysis(2016_2023)Engine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
