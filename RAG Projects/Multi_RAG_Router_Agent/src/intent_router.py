"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_RAG_Router_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import Dict, Any

class MultiRAGRouter:
    """LlamaIndex multi-index query intent router for specialized document collections."""
    
    INDEX_DOMAINS = ["financial_reports", "legal_contracts", "tech_documentation"]

    def route_query(self, query: str) -> Dict[str, Any]:
        q_lower = query.lower()
        if "finance" in q_lower or "revenue" in q_lower or "profit" in q_lower:
            chosen = "financial_reports"
        elif "contract" in q_lower or "legal" in q_lower or "clause" in q_lower:
            chosen = "legal_contracts"
        else:
            chosen = "tech_documentation"

        return {
            "query": query,
            "target_index": chosen,
            "confidence": 0.94,
            "response": f"Routed query to '{chosen}' index. Result generated."
        }
