"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: GraphRAG_KnowledgeGraph_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.graph_rag import GraphRAGEngine

def test_graph_rag():
    g = GraphRAGEngine()
    res = g.query_graph_rag("test query")
    assert len(res["subgraph_triplets"]) > 0
