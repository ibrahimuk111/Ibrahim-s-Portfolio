"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: GraphRAG_KnowledgeGraph_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.graph_rag import GraphRAGEngine

def main():
    st.set_page_config(page_title="GraphRAG Engine", page_icon="🕸️")
    st.title("🕸️ GraphRAG Knowledge Graph Engine (Neo4j + LangChain)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = GraphRAGEngine()
    q = st.text_input("Enter Query", "What treatments exist for diabetes patients?")
    
    if st.button("Query Knowledge Graph"):
        res = engine.query_graph_rag(q)
        st.subheader("Extracted Entity Triplets")
        st.json(res["subgraph_triplets"])
        st.subheader("Sub-Graph Context")
        st.code(res["augmented_context"])
        st.success(res["answer"])

if __name__ == "__main__":
    main()
