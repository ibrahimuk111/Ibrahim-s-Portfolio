"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Fact vs. Fabrication - Multi-Genre Disinformation Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Factvs.Fabrication_Multi_GenreEngine

def main():
    st.set_page_config(page_title="Fact vs. Fabrication - Multi-Genre Disinformation Detector", page_icon="🚀")
    st.title("🚀 Fact vs. Fabrication - Multi-Genre Disinformation Detector")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Factvs.Fabrication_Multi_GenreEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
