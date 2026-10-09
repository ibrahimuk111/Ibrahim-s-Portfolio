"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Chat With Multiple Documents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import ChatWithMultipleDocumentsEngine

def main():
    st.set_page_config(page_title="Chat With Multiple Documents", page_icon="🚀")
    st.title("🚀 Chat With Multiple Documents")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = ChatWithMultipleDocumentsEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
