"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Bank Marketing Campaign Analysis - Predicting Term Deposit Subscription
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import BankMarketingCampaignAnalysis_Engine

def test_engine_execution():
    engine = BankMarketingCampaignAnalysis_Engine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
