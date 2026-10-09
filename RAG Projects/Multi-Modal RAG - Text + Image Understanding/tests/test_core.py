"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi-Modal RAG - Text + Image Understanding
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import Multi_ModalRAG_Text+ImageUnderEngine

def test_engine_execution():
    engine = Multi_ModalRAG_Text+ImageUnderEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
