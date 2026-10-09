"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer Churn Prediction & Exploratory Analysis
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import CustomerChurnPrediction_ExplorEngine

def main():
    st.set_page_config(page_title="Customer Churn Prediction & Exploratory Analysis", page_icon="🚀")
    st.title("🚀 Customer Churn Prediction & Exploratory Analysis")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = CustomerChurnPrediction_ExplorEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
