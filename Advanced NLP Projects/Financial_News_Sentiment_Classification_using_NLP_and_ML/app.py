"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Financial_News_Sentiment_Classification_using_NLP_and_ML
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Financial_News_Sentiment_ClassEngine

def main():
    st.set_page_config(page_title="Financial_News_Sentiment_Classification_using_NLP_and_ML", page_icon="🚀")
    st.title("🚀 Financial_News_Sentiment_Classification_using_NLP_and_ML")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Financial_News_Sentiment_ClassEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
