"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Airbnb Price Analysis (NYC 2019)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import AirbnbPriceAnalysis(NYC2019)Engine

def test_engine_execution():
    engine = AirbnbPriceAnalysis(NYC2019)Engine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
