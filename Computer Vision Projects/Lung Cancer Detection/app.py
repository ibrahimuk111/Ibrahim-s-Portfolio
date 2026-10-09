"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Lung Cancer Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import LungCancerDetectionEngine

def main():
    st.set_page_config(page_title="Lung Cancer Detection", page_icon="🚀")
    st.title("🚀 Lung Cancer Detection")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = LungCancerDetectionEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
