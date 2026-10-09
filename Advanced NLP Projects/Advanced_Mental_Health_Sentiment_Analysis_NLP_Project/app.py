"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Advanced_Mental_Health_Sentiment_Analysis_NLP_Project
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Advanced_Mental_Health_SentimeEngine

def main():
    st.set_page_config(page_title="Advanced_Mental_Health_Sentiment_Analysis_NLP_Project", page_icon="🚀")
    st.title("🚀 Advanced_Mental_Health_Sentiment_Analysis_NLP_Project")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Advanced_Mental_Health_SentimeEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
