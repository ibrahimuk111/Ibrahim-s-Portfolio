"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: FineTuned_Medical_Legal_Specialist_LLM
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.finetune_exporter import SpecialistFineTuner

def main():
    st.set_page_config(page_title="Medical/Legal LLM Specialization", page_icon="⚖️")
    st.title("⚖️ Fine-Tuned Medical & Legal Specialist LLM (Unsloth + GGUF)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    tuner = SpecialistFineTuner()
    domain = st.selectbox("Select Domain", ["Medical", "Legal", "Financial"])
    
    if st.button("Run QLoRA Training Simulation"):
        res = tuner.simulate_fine_tuning(domain)
        st.json(res)

if __name__ == "__main__":
    main()
