"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Automatic Number Plate Recognition
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import AutomaticNumberPlateRecognitioEngine

def main():
    st.set_page_config(page_title="Automatic Number Plate Recognition", page_icon="🚀")
    st.title("🚀 Automatic Number Plate Recognition")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = AutomaticNumberPlateRecognitioEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
