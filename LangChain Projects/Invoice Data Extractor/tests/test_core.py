"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Invoice Data Extractor
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import InvoiceDataExtractorEngine

def test_engine_execution():
    engine = InvoiceDataExtractorEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
