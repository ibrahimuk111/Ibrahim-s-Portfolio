"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Chain-of-Thought & Self-Consistency
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Chain_of_Thought_Self_ConsisteEngine

def main():
    st.set_page_config(page_title="Chain-of-Thought & Self-Consistency", page_icon="🚀")
    st.title("🚀 Chain-of-Thought & Self-Consistency")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Chain_of_Thought_Self_ConsisteEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
