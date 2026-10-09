"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: XAI_Model_Interpretability_Dashboard
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.explainability import TabularExplainer

def test_explainer():
    exp = TabularExplainer(["f1", "f2"])
    shaps = exp.get_shap_values([10, 20])
    assert "f1" in shaps and "f2" in shaps
