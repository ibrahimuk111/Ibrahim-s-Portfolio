"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Differential_Privacy_ML_Classifier
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.dp_classifier import DifferentialPrivacyModel

def test_dp():
    m = DifferentialPrivacyModel()
    res = m.train_with_privacy(1.0)
    assert res["epsilon_privacy_budget"] == 1.0
