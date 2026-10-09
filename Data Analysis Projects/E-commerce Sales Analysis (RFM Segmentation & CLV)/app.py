"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: E-commerce Sales Analysis (RFM Segmentation & CLV)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import E_commerceSalesAnalysis(RFMSegEngine

def main():
    st.set_page_config(page_title="E-commerce Sales Analysis (RFM Segmentation & CLV)", page_icon="🚀")
    st.title("🚀 E-commerce Sales Analysis (RFM Segmentation & CLV)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = E_commerceSalesAnalysis(RFMSegEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
