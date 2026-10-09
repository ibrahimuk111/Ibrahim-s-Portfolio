"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Airbnb Price Analysis (NYC 2019)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import AirbnbPriceAnalysis(NYC2019)Engine

def main():
    st.set_page_config(page_title="Airbnb Price Analysis (NYC 2019)", page_icon="🚀")
    st.title("🚀 Airbnb Price Analysis (NYC 2019)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = AirbnbPriceAnalysis(NYC2019)Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
