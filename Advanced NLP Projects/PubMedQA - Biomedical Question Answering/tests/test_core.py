"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: PubMedQA - Biomedical Question Answering
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import PubMedQA_BiomedicalQuestionAnsEngine

def test_engine_execution():
    engine = PubMedQA_BiomedicalQuestionAnsEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
