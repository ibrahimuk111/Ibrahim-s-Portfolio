"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Advanced_Human_vs_AI_Text_ClasEngine

def main():
    st.set_page_config(page_title="Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT", page_icon="🚀")
    st.title("🚀 Advanced_Human_vs_AI_Text_Classifier_using_NLP_and_BERT")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Advanced_Human_vs_AI_Text_ClasEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
