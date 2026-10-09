"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Adversarial_Attack_Defense_CV
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.adversarial import AdversarialRobustness

def test_robustness():
    adv = AdversarialRobustness()
    res = adv.evaluate_defense(0.90, 0.1)
    assert res["adversarial_accuracy"] < 0.90
    assert res["defended_accuracy"] >= res["adversarial_accuracy"]
