"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Car Detection using Drone
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import CarDetectionusingDroneEngine

def main():
    st.set_page_config(page_title="Car Detection using Drone", page_icon="🚀")
    st.title("🚀 Car Detection using Drone")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = CarDetectionusingDroneEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
