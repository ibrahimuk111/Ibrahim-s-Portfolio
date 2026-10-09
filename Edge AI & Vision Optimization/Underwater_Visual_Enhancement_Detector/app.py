"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Underwater_Visual_Enhancement_Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
import numpy as np
from src.enhancement import UnderwaterEnhancer

def main():
    st.set_page_config(page_title="Underwater Enhancement", page_icon="🌊")
    st.title("🌊 Underwater Visual Enhancement & Object Detector")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    enhancer = UnderwaterEnhancer()
    
    if st.button("Process Underwater Frame"):
        fake_img = np.random.randint(0, 255, (300, 300, 3), dtype=np.uint8)
        res = enhancer.enhance_frame(fake_img)
        c1, c2 = st.columns(2)
        c1.metric("Original Contrast", res["original_contrast"])
        c2.metric("Enhanced Contrast", res["enhanced_contrast"])

if __name__ == "__main__":
    main()
