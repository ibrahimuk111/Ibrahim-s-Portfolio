"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Secure_MultiParty_Computation_Analytics
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.smpc import SMPCAnalytics

def test_smpc():
    s = SMPCAnalytics()
    res = s.secret_share_mean([10.0, 20.0, 30.0])
    assert res["computed_secure_mean"] == 20.0
