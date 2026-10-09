"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Predictive Maintenance - Machine Failure Classification
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import PredictiveMaintenance_MachineFEngine

def main():
    st.set_page_config(page_title="Predictive Maintenance - Machine Failure Classification", page_icon="🚀")
    st.title("🚀 Predictive Maintenance - Machine Failure Classification")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = PredictiveMaintenance_MachineFEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
