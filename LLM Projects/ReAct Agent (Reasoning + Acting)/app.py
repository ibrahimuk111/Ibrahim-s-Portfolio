"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: ReAct Agent (Reasoning + Acting)
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import ReActAgent(Reasoning+Acting)Engine

def main():
    st.set_page_config(page_title="ReAct Agent (Reasoning + Acting)", page_icon="🚀")
    st.title("🚀 ReAct Agent (Reasoning + Acting)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = ReActAgent(Reasoning+Acting)Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
