"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Conversational Memory with Summarization
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import ConversationalMemorywithSummarEngine

def main():
    st.set_page_config(page_title="Conversational Memory with Summarization", page_icon="🚀")
    st.title("🚀 Conversational Memory with Summarization")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = ConversationalMemorywithSummarEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
