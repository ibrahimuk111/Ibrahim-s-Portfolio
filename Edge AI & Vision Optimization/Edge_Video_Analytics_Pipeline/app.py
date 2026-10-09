"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Edge_Video_Analytics_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.analytics import VideoAnalyticsEngine

def main():
    st.set_page_config(page_title="Edge Video Analytics", page_icon="📹")
    st.title("📹 Edge Video Analytics & Action Recognition Pipeline")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = VideoAnalyticsEngine()
    
    if st.button("Analyze Edge Stream"):
        res = engine.analyze_stream("camera_gate_01")
        c1, c2, c3 = st.columns(3)
        c1.metric("People Count", res["people_count"])
        c2.metric("Vehicle Count", res["vehicle_count"])
        c3.metric("Edge GPU Util", f"{res['gpu_utilization_pct']}%")
        st.json(res)

if __name__ == "__main__":
    main()
