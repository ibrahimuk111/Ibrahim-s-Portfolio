"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Function Calling  Tool Use with Llama 3.1
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import FunctionCallingToolUsewithLlamEngine

def main():
    st.set_page_config(page_title="Function Calling  Tool Use with Llama 3.1", page_icon="🚀")
    st.title("🚀 Function Calling  Tool Use with Llama 3.1")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = FunctionCallingToolUsewithLlamEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
