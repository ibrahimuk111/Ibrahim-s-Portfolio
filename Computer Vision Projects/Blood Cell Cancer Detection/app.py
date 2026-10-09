"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Blood Cell Cancer Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import BloodCellCancerDetectionEngine

def main():
    st.set_page_config(page_title="Blood Cell Cancer Detection", page_icon="🚀")
    st.title("🚀 Blood Cell Cancer Detection")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = BloodCellCancerDetectionEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
