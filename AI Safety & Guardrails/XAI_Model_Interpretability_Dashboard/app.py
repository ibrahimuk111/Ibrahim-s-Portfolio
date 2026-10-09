"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: XAI_Model_Interpretability_Dashboard
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.explainability import TabularExplainer

def main():
    st.set_page_config(page_title="XAI Dashboard", page_icon="🧠")
    st.title("🧠 XAI Model Interpretability Dashboard (SHAP & LIME)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    features = ["Age", "Income", "Credit_Score", "Debt_Ratio"]
    explainer = TabularExplainer(features)
    
    st.subheader("Input Sample Features")
    age = st.slider("Age", 18, 80, 35)
    income = st.slider("Income ($k)", 10, 200, 75)
    credit = st.slider("Credit Score", 300, 850, 720)
    debt = st.slider("Debt Ratio", 0.0, 1.0, 0.3)
    
    if st.button("Generate Feature Attributions"):
        shaps = explainer.get_shap_values([age, income, credit, debt])
        st.subheader("Feature Importance (SHAP Values)")
        st.bar_chart(shaps)

if __name__ == "__main__":
    main()
