"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Face Liveness Detection System
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import FaceLivenessDetectionSystemEngine

def main():
    st.set_page_config(page_title="Face Liveness Detection System", page_icon="🚀")
    st.title("🚀 Face Liveness Detection System")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = FaceLivenessDetectionSystemEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
