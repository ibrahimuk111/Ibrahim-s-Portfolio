"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Eye Diseases Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import EyeDiseasesDetectionEngine

def main():
    st.set_page_config(page_title="Eye Diseases Detection", page_icon="🚀")
    st.title("🚀 Eye Diseases Detection")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = EyeDiseasesDetectionEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
