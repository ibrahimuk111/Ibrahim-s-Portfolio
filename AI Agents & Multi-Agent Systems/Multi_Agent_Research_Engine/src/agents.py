"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Agent_Research_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import os
from typing import List, Dict, Any


class ResearchAgent:
    """Agent responsible for web research using Tavily API."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("TAVILY_API_KEY", "")
        self.search_results: List[Dict[str, Any]] = []

    def search(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """Execute a research query and return structured results."""
        try:
            from tavily import TavilyClient
            client = TavilyClient(api_key=self.api_key)
            response = client.search(query=query, max_results=max_results)
            self.search_results = response.get("results", [])
        except ImportError:
            self.search_results = [{"title": "Mock Result", "url": "https://example.com",
                                     "content": f"Simulated research result for: {query}"}]
        return self.search_results


class SynthesisAgent:
    """Agent that synthesizes research findings into coherent reports."""

    def __init__(self, llm_provider: str = "openai"):
        self.llm_provider = llm_provider
        self.synthesis_history: List[str] = []

    def synthesize(self, findings: List[Dict[str, Any]], topic: str) -> str:
        """Synthesize multiple research findings into a report."""
        report_parts = [f"# Research Report: {topic}\n"]
        for i, finding in enumerate(findings, 1):
            title = finding.get("title", "Untitled")
            content = finding.get("content", "No content available.")
            report_parts.append(f"## Finding {i}: {title}\n{content}\n")
        report = "\n".join(report_parts)
        self.synthesis_history.append(report)
        return report


class CriticAgent:
    """Agent that reviews and critiques synthesized reports for quality."""

    def __init__(self):
        self.reviews: List[Dict[str, Any]] = []

    def review(self, report: str) -> Dict[str, Any]:
        """Review a report and provide quality assessment."""
        word_count = len(report.split())
        has_sections = report.count("##") > 0
        score = min(10, max(1, word_count // 50 + (3 if has_sections else 0)))
        review = {
            "word_count": word_count,
            "has_structure": has_sections,
            "quality_score": score,
            "feedback": "Well-structured report." if score >= 6 else "Needs more depth.",
            "approved": score >= 5
        }
        self.reviews.append(review)
        return review
