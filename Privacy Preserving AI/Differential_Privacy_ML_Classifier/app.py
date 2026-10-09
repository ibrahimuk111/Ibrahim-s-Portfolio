"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Differential_Privacy_ML_Classifier
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.dp_classifier import DifferentialPrivacyModel

def main():
    st.set_page_config(page_title="Differential Privacy Classifier", page_icon="🔐")
    st.title("🔐 Differential Privacy ML Classifier (Opacus / PyTorch)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    model = DifferentialPrivacyModel()
    eps = st.slider("Epsilon (Privacy Budget ε)", 0.1, 10.0, 1.0, 0.1)
    
    if st.button("Train Privately"):
        res = model.train_with_privacy(eps)
        st.json(res)

if __name__ == "__main__":
    main()
