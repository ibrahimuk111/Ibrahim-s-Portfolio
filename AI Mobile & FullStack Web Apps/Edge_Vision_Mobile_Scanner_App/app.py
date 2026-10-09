"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Edge_Vision_Mobile_Scanner_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.onnx_mobile import ONNXMobileScanner

def main():
    st.set_page_config(page_title="Edge Mobile Scanner", page_icon="📱")
    st.title("📱 Edge Vision Mobile Scanner (ONNX Runtime)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    scanner = ONNXMobileScanner()
    
    if st.button("Simulate Offline Camera Scan"):
        res = scanner.scan_camera_frame()
        st.json(res)

if __name__ == "__main__":
    main()
