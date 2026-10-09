"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: HR Analytics - Employee Attrition & Performance
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import HRAnalytics_EmployeeAttrition_Engine

def main():
    st.set_page_config(page_title="HR Analytics - Employee Attrition & Performance", page_icon="🚀")
    st.title("🚀 HR Analytics - Employee Attrition & Performance")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = HRAnalytics_EmployeeAttrition_Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
