"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_RAG_Router_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.intent_router import MultiRAGRouter

def test_router():
    r = MultiRAGRouter()
    res = r.route_query("legal contracts clause")
    assert res["target_index"] == "legal_contracts"
