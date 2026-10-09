"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer_Support_Swarm_Agents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

﻿"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer_Support_Swarm_Agents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import Dict, Any, List
from dataclasses import dataclass
import re


@dataclass
class RoutingDecision:
    domain: str
    confidence: float
    reasoning: str
    query: str


class RouterAgent:
    """Routes customer queries to specialized domain agents."""

    DOMAIN_KEYWORDS = {
        "billing": ["bill", "invoice", "payment", "charge", "refund", "subscription", "price"],
        "technical": ["error", "bug", "crash", "install", "update", "not working", "broken", "slow"],
        "shipping": ["delivery", "ship", "track", "package", "order", "return", "lost"],
        "general": ["info", "hours", "contact", "about", "help"],
    }

    def route(self, query: str) -> RoutingDecision:
        query_lower = query.lower()
        scores: Dict[str, int] = {}
        for domain, keywords in self.DOMAIN_KEYWORDS.items():
            scores[domain] = sum(1 for kw in keywords if kw in query_lower)

        best_domain = max(scores, key=scores.get)
        total = sum(scores.values()) or 1
        confidence = scores[best_domain] / total if scores[best_domain] > 0 else 0.25

        if scores[best_domain] == 0:
            best_domain = "general"
            confidence = 0.25

        return RoutingDecision(
            domain=best_domain, confidence=confidence,
            reasoning=f"Matched {scores[best_domain]} keywords for '{best_domain}'",
            query=query
        )
