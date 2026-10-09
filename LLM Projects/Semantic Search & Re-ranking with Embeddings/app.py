"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Semantic Search & Re-ranking with Embeddings
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import SemanticSearch_Re_rankingwithEEngine

def main():
    st.set_page_config(page_title="Semantic Search & Re-ranking with Embeddings", page_icon="🚀")
    st.title("🚀 Semantic Search & Re-ranking with Embeddings")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = SemanticSearch_Re_rankingwithEEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
