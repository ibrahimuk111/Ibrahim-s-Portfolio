"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: The Core Memory Bank (PDF Document Q&A)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import TheCoreMemoryBank(PDFDocumentQEngine

def main():
    st.set_page_config(page_title="The Core Memory Bank (PDF Document Q&A)", page_icon="🚀")
    st.title("🚀 The Core Memory Bank (PDF Document Q&A)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = TheCoreMemoryBank(PDFDocumentQEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
