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

import pytest
from src.agents import ResearchAgent, SynthesisAgent, CriticAgent
from src.orchestrator import MultiAgentOrchestrator


class TestResearchAgent:
    def test_search_returns_results(self):
        agent = ResearchAgent()
        results = agent.search("test query")
        assert isinstance(results, list)
        assert len(results) > 0

    def test_search_result_structure(self):
        agent = ResearchAgent()
        results = agent.search("AI research")
        for r in results:
            assert "content" in r


class TestSynthesisAgent:
    def test_synthesize_creates_report(self):
        agent = SynthesisAgent()
        findings = [{"title": "Test", "content": "Test content"}]
        report = agent.synthesize(findings, "Test Topic")
        assert "Test Topic" in report
        assert len(report) > 0

    def test_synthesis_history(self):
        agent = SynthesisAgent()
        agent.synthesize([{"title": "A", "content": "B"}], "Topic")
        assert len(agent.synthesis_history) == 1


class TestCriticAgent:
    def test_review_returns_score(self):
        agent = CriticAgent()
        review = agent.review("## Section\nThis is a well-written report with many words " * 10)
        assert "quality_score" in review
        assert 1 <= review["quality_score"] <= 10


class TestOrchestrator:
    def test_pipeline_completes(self):
        orch = MultiAgentOrchestrator()
        result = orch.run_pipeline("test topic")
        assert "report" in result
        assert "review" in result
        assert result["iterations"] >= 1
