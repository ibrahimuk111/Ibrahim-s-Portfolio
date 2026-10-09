"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Wine Quality Prediction - EDA & Classification
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import WineQualityPrediction_EDA_ClasEngine

def main():
    st.set_page_config(page_title="Wine Quality Prediction - EDA & Classification", page_icon="🚀")
    st.title("🚀 Wine Quality Prediction - EDA & Classification")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = WineQualityPrediction_EDA_ClasEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
