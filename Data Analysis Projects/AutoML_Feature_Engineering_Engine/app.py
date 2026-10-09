"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: AutoML_Feature_Engineering_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.automl_engine import AutoMLFeatureEngine

def main():
    st.set_page_config(page_title="AutoML Feature Engine", page_icon="⚙️")
    st.title("⚙️ AutoML & Automated Feature Engineering Engine (Optuna)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = AutoMLFeatureEngine()
    metric = st.selectbox("Optimization Metric", ["roc_auc", "accuracy", "f1_score"])
    
    if st.button("Run AutoML Pipeline"):
        res = engine.run_automl_pipeline(metric)
        st.json(res)

if __name__ == "__main__":
    main()
