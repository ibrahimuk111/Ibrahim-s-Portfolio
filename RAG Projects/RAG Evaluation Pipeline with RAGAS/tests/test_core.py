"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RAG Evaluation Pipeline with RAGAS
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import RAGEvaluationPipelinewithRAGASEngine

def test_engine_execution():
    engine = RAGEvaluationPipelinewithRAGASEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
