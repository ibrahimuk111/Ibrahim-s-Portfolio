"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RAG Evaluation Pipeline with RAGAS
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import RAGEvaluationPipelinewithRAGASEngine

def main():
    st.set_page_config(page_title="RAG Evaluation Pipeline with RAGAS", page_icon="🚀")
    st.title("🚀 RAG Evaluation Pipeline with RAGAS")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = RAGEvaluationPipelinewithRAGASEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
