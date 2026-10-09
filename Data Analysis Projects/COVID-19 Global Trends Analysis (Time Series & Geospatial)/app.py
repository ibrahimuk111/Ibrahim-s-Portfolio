"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: COVID-19 Global Trends Analysis (Time Series & Geospatial)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import COVID_19GlobalTrendsAnalysis(TEngine

def main():
    st.set_page_config(page_title="COVID-19 Global Trends Analysis (Time Series & Geospatial)", page_icon="🚀")
    st.title("🚀 COVID-19 Global Trends Analysis (Time Series & Geospatial)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = COVID_19GlobalTrendsAnalysis(TEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
