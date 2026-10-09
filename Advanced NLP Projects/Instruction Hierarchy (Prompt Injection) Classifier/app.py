"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Instruction Hierarchy (Prompt Injection) Classifier
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import InstructionHierarchy(PromptInjEngine

def main():
    st.set_page_config(page_title="Instruction Hierarchy (Prompt Injection) Classifier", page_icon="🚀")
    st.title("🚀 Instruction Hierarchy (Prompt Injection) Classifier")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = InstructionHierarchy(PromptInjEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
