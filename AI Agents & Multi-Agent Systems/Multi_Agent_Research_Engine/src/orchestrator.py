"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Agent_Research_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

﻿"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Agent_Research_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import Dict, Any, Optional
from src.agents import ResearchAgent, SynthesisAgent, CriticAgent


class MultiAgentOrchestrator:
    """Orchestrates multi-agent research workflow using a graph-based approach."""

    def __init__(self, tavily_key: str = None):
        self.researcher = ResearchAgent(api_key=tavily_key)
        self.synthesizer = SynthesisAgent()
        self.critic = CriticAgent()
        self.state: Dict[str, Any] = {"status": "idle"}

    def run_pipeline(self, topic: str, max_results: int = 5,
                     max_iterations: int = 3) -> Dict[str, Any]:
        """Execute the full multi-agent research pipeline."""
        self.state["status"] = "researching"
        findings = self.researcher.search(topic, max_results=max_results)

        for iteration in range(max_iterations):
            self.state["status"] = f"synthesizing (iteration {iteration + 1})"
            report = self.synthesizer.synthesize(findings, topic)

            self.state["status"] = f"reviewing (iteration {iteration + 1})"
            review = self.critic.review(report)

            if review["approved"]:
                self.state["status"] = "completed"
                return {
                    "topic": topic,
                    "report": report,
                    "review": review,
                    "iterations": iteration + 1,
                    "findings_count": len(findings)
                }

        self.state["status"] = "completed_with_warnings"
        return {"topic": topic, "report": report, "review": review,
                "iterations": max_iterations, "findings_count": len(findings)}
