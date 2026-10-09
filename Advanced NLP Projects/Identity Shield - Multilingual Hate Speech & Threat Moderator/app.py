"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Identity Shield - Multilingual Hate Speech & Threat Moderator
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import IdentityShield_MultilingualHatEngine

def main():
    st.set_page_config(page_title="Identity Shield - Multilingual Hate Speech & Threat Moderator", page_icon="🚀")
    st.title("🚀 Identity Shield - Multilingual Hate Speech & Threat Moderator")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = IdentityShield_MultilingualHatEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
