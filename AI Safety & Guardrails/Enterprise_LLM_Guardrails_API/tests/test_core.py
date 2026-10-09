"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_LLM_Guardrails_API
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import pytest
from src.guardrails import SafetyGuardrails

def test_pii_masking():
    guard = SafetyGuardrails()
    text = "Contact user at john@example.com or 555-123-4567"
    res = guard.mask_pii(text)
    assert "[REDACTED_EMAIL]" in res
    assert "[REDACTED_PHONE]" in res

def test_toxicity_check():
    guard = SafetyGuardrails()
    res = guard.check_toxicity("This contains malware attack instructions")
    assert res["is_safe"] is False
    assert len(res["flagged_keywords"]) >= 1
