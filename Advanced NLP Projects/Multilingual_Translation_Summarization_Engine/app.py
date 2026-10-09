"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multilingual_Translation_Summarization_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.translation_engine import MultilingualEngine

def main():
    st.set_page_config(page_title="Multilingual NLP Engine", page_icon="🌐")
    st.title("🌐 Multilingual Translation & Summarization Engine")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = MultilingualEngine()
    t = st.text_area("Input Document Text", "Artificial intelligence continues to transform modern software engineering...")
    lang = st.selectbox("Target Language", ["Spanish (es)", "French (fr)", "German (de)", "Urdu (ur)"])
    
    if st.button("Process Document"):
        res = engine.translate_and_summarize(t, lang)
        st.json(res)

if __name__ == "__main__":
    main()
