"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_RAG_Router_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.intent_router import MultiRAGRouter

def main():
    st.set_page_config(page_title="Multi-RAG Router Agent", page_icon="🔀")
    st.title("🔀 Multi-RAG Router Agent (LlamaIndex Intent Routing)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    router = MultiRAGRouter()
    q = st.text_input("Enter Query", "What was the Q3 revenue increase?")
    
    if st.button("Route Query"):
        res = router.route_query(q)
        st.metric("Target Index Routed", res["target_index"])
        st.success(res["response"])

if __name__ == "__main__":
    main()
