"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RAG_Hallucination_Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.evaluator import HallucinationDetector

def test_evaluator():
    det = HallucinationDetector()
    f = det.evaluate_faithfulness("Paris is in France", "Paris is in France")
    assert f["faithfulness_score"] >= 0.8
    r = det.evaluate_relevancy("capital of France", "Paris is capital of France")
    assert r["relevancy_score"] >= 0.3
