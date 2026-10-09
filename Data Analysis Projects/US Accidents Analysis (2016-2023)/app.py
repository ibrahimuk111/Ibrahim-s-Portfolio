"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: US Accidents Analysis (2016-2023)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import USAccidentsAnalysis(2016_2023)Engine

def main():
    st.set_page_config(page_title="US Accidents Analysis (2016-2023)", page_icon="🚀")
    st.title("🚀 US Accidents Analysis (2016-2023)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = USAccidentsAnalysis(2016_2023)Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
