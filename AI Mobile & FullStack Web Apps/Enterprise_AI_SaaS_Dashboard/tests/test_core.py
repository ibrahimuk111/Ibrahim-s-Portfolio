"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_AI_SaaS_Dashboard
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.saas_engine import EnterpriseSaaSEngine

def test_saas_billing():
    e = EnterpriseSaaSEngine()
    res = e.verify_and_consume("user123", "pro", 500)
    assert res["authorized"] is True
    
    res_exceeded = e.verify_and_consume("user123", "free", 500)
    assert res_exceeded["authorized"] is False
