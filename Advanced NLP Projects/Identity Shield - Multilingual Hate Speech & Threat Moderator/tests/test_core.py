"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Identity Shield - Multilingual Hate Speech & Threat Moderator
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import IdentityShield_MultilingualHatEngine

def test_engine_execution():
    engine = IdentityShield_MultilingualHatEngine()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "Muhammad Ibrahim"
