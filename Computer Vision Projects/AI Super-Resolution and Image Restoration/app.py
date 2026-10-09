"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: AI Super-Resolution and Image Restoration
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import AISuper_ResolutionandImageRestEngine

def main():
    st.set_page_config(page_title="AI Super-Resolution and Image Restoration", page_icon="🚀")
    st.title("🚀 AI Super-Resolution and Image Restoration")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = AISuper_ResolutionandImageRestEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
