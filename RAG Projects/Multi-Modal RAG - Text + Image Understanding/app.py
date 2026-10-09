"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi-Modal RAG - Text + Image Understanding
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Multi_ModalRAG_Text+ImageUnderEngine

def main():
    st.set_page_config(page_title="Multi-Modal RAG - Text + Image Understanding", page_icon="🚀")
    st.title("🚀 Multi-Modal RAG - Text + Image Understanding")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Multi_ModalRAG_Text+ImageUnderEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
