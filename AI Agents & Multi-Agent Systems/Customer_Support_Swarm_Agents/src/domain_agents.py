"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer_Support_Swarm_Agents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class AgentResponse:
    domain: str
    message: str
    suggested_actions: list
    escalate: bool = False


class BillingAgent:
    """Handles billing, payment, and subscription queries."""

    def respond(self, query: str) -> AgentResponse:
        return AgentResponse(
            domain="billing",
            message=f"I can help with your billing concern. Regarding: '{query}' - "
                    f"Let me pull up your account details and recent transactions.",
            suggested_actions=["View recent invoices", "Update payment method", "Request refund"]
        )


class TechnicalAgent:
    """Handles technical support and troubleshooting."""

    def respond(self, query: str) -> AgentResponse:
        return AgentResponse(
            domain="technical",
            message=f"I'll help troubleshoot your issue: '{query}'. "
                    f"Let's start with some diagnostic steps.",
            suggested_actions=["Check system status", "Clear cache", "Update software",
                             "Contact engineering"]
        )


class ShippingAgent:
    """Handles shipping, delivery, and order queries."""

    def respond(self, query: str) -> AgentResponse:
        return AgentResponse(
            domain="shipping",
            message=f"I can help track your order. Regarding: '{query}' - "
                    f"Let me check the shipping status.",
            suggested_actions=["Track package", "Request return label", "File missing item report"]
        )


class GeneralAgent:
    """Handles general inquiries and fallback."""

    def respond(self, query: str) -> AgentResponse:
        return AgentResponse(
            domain="general",
            message=f"Thank you for reaching out. Regarding: '{query}' - "
                    f"I'll do my best to assist you.",
            suggested_actions=["FAQ", "Contact human agent", "Submit feedback"],
            escalate=True
        )
