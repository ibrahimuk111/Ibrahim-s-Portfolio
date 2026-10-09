"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: FineTuned_Medical_Legal_Specialist_LLM
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.finetune_exporter import SpecialistFineTuner

def test_finetune():
    t = SpecialistFineTuner()
    res = t.simulate_fine_tuning("Medical")
    assert res["status"] == "FINE_TUNING_COMPLETE"
