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

from typing import Dict, Any
from src.router_agent import RouterAgent, RoutingDecision
from src.domain_agents import BillingAgent, TechnicalAgent, ShippingAgent, GeneralAgent, AgentResponse


class SwarmController:
    """Controls the swarm of specialized customer support agents."""

    def __init__(self):
        self.router = RouterAgent()
        self.agents = {
            "billing": BillingAgent(),
            "technical": TechnicalAgent(),
            "shipping": ShippingAgent(),
            "general": GeneralAgent(),
        }
        self.interaction_log = []

    def handle_query(self, query: str) -> Dict[str, Any]:
        routing = self.router.route(query)
        agent = self.agents.get(routing.domain, self.agents["general"])
        response = agent.respond(query)

        result = {
            "routing": {"domain": routing.domain, "confidence": routing.confidence,
                        "reasoning": routing.reasoning},
            "response": {"message": response.message, "actions": response.suggested_actions,
                         "escalate": response.escalate}
        }
        self.interaction_log.append(result)
        return result

    def get_analytics(self) -> Dict[str, Any]:
        if not self.interaction_log:
            return {"total": 0, "domains": {}}
        domains = {}
        for log in self.interaction_log:
            d = log["routing"]["domain"]
            domains[d] = domains.get(d, 0) + 1
        return {"total": len(self.interaction_log), "domains": domains}
