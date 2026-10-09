"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Enterprise_LLM_Guardrails_API
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import re
from typing import Dict, Any, List

class SafetyGuardrails:
    """Enterprise safety, toxicity filtering, and PII masking pipeline."""
    
    PII_PATTERNS = {
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
        "ssn": r"\b\d{3}-\d{2}-\d{4}\b"
    }
    
    TOXIC_KEYWORDS = ["harm", "hate", "exploit", "attack", "malware", "bypass"]
    
    def mask_pii(self, text: str) -> str:
        masked = text
        for pii_type, pattern in self.PII_PATTERNS.items():
            masked = re.sub(pattern, f"[REDACTED_{pii_type.upper()}]", masked)
        return masked

    def check_toxicity(self, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        flagged = [kw for kw in self.TOXIC_KEYWORDS if kw in text_lower]
        is_safe = len(flagged) == 0
        return {
            "is_safe": is_safe,
            "toxicity_score": len(flagged) / max(len(self.TOXIC_KEYWORDS), 1),
            "flagged_keywords": flagged
        }

    def sanitize(self, text: str) -> Dict[str, Any]:
        tox = self.check_toxicity(text)
        masked_text = self.mask_pii(text)
        return {
            "original_text": text,
            "sanitized_text": masked_text,
            "is_safe": tox["is_safe"],
            "toxicity_score": tox["toxicity_score"],
            "flagged_keywords": tox["flagged_keywords"]
        }
