"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: AutoML_Feature_Engineering_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.automl_engine import AutoMLFeatureEngine

def test_automl():
    a = AutoMLFeatureEngine()
    res = a.run_automl_pipeline()
    assert res["best_score"] > 0.8
