"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Global Superstore Sales Analysis
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import GlobalSuperstoreSalesAnalysisEngine

def main():
    st.set_page_config(page_title="Global Superstore Sales Analysis", page_icon="🚀")
    st.title("🚀 Global Superstore Sales Analysis")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = GlobalSuperstoreSalesAnalysisEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
