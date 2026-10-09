"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Codebasics FAQ Chatbot
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import CodebasicsFAQChatbotEngine

def main():
    st.set_page_config(page_title="Codebasics FAQ Chatbot", page_icon="🚀")
    st.title("🚀 Codebasics FAQ Chatbot")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = CodebasicsFAQChatbotEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
