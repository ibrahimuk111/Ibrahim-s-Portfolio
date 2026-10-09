"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Automated_Data_Model_Drift_Monitor
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.drift_detector import DriftMonitor

def test_drift():
    m = DriftMonitor()
    ref = [1.0] * 100
    curr = [5.0] * 100
    res = m.calculate_ks_drift(ref, curr)
    assert res["is_drifted"] is True
