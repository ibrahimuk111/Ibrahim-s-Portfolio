"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer_Support_Swarm_Agents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import pytest
from src.router_agent import RouterAgent
from src.domain_agents import BillingAgent, TechnicalAgent, ShippingAgent
from src.swarm_controller import SwarmController


class TestRouterAgent:
    def test_routes_billing(self):
        router = RouterAgent()
        result = router.route("I need a refund for my payment")
        assert result.domain == "billing"

    def test_routes_technical(self):
        router = RouterAgent()
        result = router.route("The app is crashing with an error")
        assert result.domain == "technical"

    def test_routes_shipping(self):
        router = RouterAgent()
        result = router.route("Where is my delivery?")
        assert result.domain == "shipping"

    def test_fallback_to_general(self):
        router = RouterAgent()
        result = router.route("xyz abc random")
        assert result.domain == "general"


class TestSwarmController:
    def test_handle_query(self):
        controller = SwarmController()
        result = controller.handle_query("I need help with my bill")
        assert "routing" in result
        assert "response" in result

    def test_analytics(self):
        controller = SwarmController()
        controller.handle_query("refund")
        controller.handle_query("error")
        analytics = controller.get_analytics()
        assert analytics["total"] == 2
