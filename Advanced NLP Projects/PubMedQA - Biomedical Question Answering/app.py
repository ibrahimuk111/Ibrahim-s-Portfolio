"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: PubMedQA - Biomedical Question Answering
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import PubMedQA_BiomedicalQuestionAnsEngine

def main():
    st.set_page_config(page_title="PubMedQA - Biomedical Question Answering", page_icon="🚀")
    st.title("🚀 PubMedQA - Biomedical Question Answering")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = PubMedQA_BiomedicalQuestionAnsEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
