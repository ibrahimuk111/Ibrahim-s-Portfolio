"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: The Financial Analyst - Natural Language to SQL with LLM
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import TheFinancialAnalyst_NaturalLanEngine

def main():
    st.set_page_config(page_title="The Financial Analyst - Natural Language to SQL with LLM", page_icon="🚀")
    st.title("🚀 The Financial Analyst - Natural Language to SQL with LLM")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = TheFinancialAnalyst_NaturalLanEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
