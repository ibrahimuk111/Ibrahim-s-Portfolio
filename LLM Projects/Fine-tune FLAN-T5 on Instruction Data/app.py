"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Fine-tune FLAN-T5 on Instruction Data
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import Fine_tuneFLAN_T5onInstructionDEngine

def main():
    st.set_page_config(page_title="Fine-tune FLAN-T5 on Instruction Data", page_icon="🚀")
    st.title("🚀 Fine-tune FLAN-T5 on Instruction Data")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = Fine_tuneFLAN_T5onInstructionDEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
