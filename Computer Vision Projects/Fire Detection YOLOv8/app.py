"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Fire Detection YOLOv8
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import FireDetectionYOLOv8Engine

def main():
    st.set_page_config(page_title="Fire Detection YOLOv8", page_icon="🚀")
    st.title("🚀 Fire Detection YOLOv8")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = FireDetectionYOLOv8Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
