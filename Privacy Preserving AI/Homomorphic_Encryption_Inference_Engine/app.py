"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Homomorphic_Encryption_Inference_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.homomorphic import HomomorphicInferenceEngine

def main():
    st.set_page_config(page_title="Homomorphic Encryption Inference", page_icon="🔑")
    st.title("🔑 Homomorphic Encryption Inference Engine (TenSEAL)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = HomomorphicInferenceEngine()
    
    if st.button("Execute Encrypted Inference"):
        res = engine.run_encrypted_inference(128)
        st.json(res)

if __name__ == "__main__":
    main()
