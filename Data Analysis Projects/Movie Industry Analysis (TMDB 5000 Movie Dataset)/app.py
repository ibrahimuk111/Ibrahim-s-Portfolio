"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Movie Industry Analysis (TMDB 5000 Movie Dataset)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import MovieIndustryAnalysis(TMDB5000Engine

def main():
    st.set_page_config(page_title="Movie Industry Analysis (TMDB 5000 Movie Dataset)", page_icon="🚀")
    st.title("🚀 Movie Industry Analysis (TMDB 5000 Movie Dataset)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = MovieIndustryAnalysis(TMDB5000Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
