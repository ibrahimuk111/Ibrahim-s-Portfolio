"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: House Price Prediction (Regression)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import HousePricePrediction(RegressioEngine

def main():
    st.set_page_config(page_title="House Price Prediction (Regression)", page_icon="🚀")
    st.title("🚀 House Price Prediction (Regression)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = HousePricePrediction(RegressioEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
