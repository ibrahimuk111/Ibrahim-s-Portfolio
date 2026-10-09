"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Fact vs. Fabrication - Multi-Genre Disinformation Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Factvs.Fabrication_Multi_GenreEngine

def test_engine_execution():
    engine = Factvs.Fabrication_Multi_GenreEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
