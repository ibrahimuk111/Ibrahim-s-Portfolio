"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Adversarial_Attack_Defense_CV
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.adversarial import AdversarialRobustness

def main():
    st.set_page_config(page_title="Adversarial Attack & Defense CV", page_icon="🛡️")
    st.title("🛡️ Adversarial Attack & Defense Engine (CV)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = AdversarialRobustness()
    eps = st.slider("Epsilon (Perturbation Intensity)", 0.01, 0.30, 0.05, 0.01)
    
    if st.button("Run Robustness Benchmark"):
        res = engine.evaluate_defense(0.95, eps)
        c1, c2, c3 = st.columns(3)
        c1.metric("Clean Accuracy", f"{res['original_accuracy']:.0%}")
        c2.metric("Adversarial Accuracy", f"{res['adversarial_accuracy']:.0%}")
        c3.metric("Defended Accuracy", f"{res['defended_accuracy']:.0%}")

if __name__ == "__main__":
    main()
