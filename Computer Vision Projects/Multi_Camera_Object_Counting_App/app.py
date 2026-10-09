"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Camera_Object_Counting_App
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.multi_camera_counter import MultiCameraCounter

def main():
    st.set_page_config(page_title="Multi-Camera Counter", page_icon="📹")
    st.title("📹 Multi-Camera Object Counting Engine (YOLOv8 + DeepSORT)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    counter = MultiCameraCounter()
    cam = st.selectbox("Select Camera Stream", ["Cam_01_NorthGate", "Cam_02_SouthGate", "Cam_03_Lobby"])
    
    if st.button("Fetch Real-Time Zone Analytics"):
        res = counter.process_camera_stream(cam)
        c1, c2, c3 = st.columns(3)
        c1.metric("Entered", res["in_count"])
        c2.metric("Exited", res["out_count"])
        c3.metric("Current Occupancy", res["current_occupancy"])

if __name__ == "__main__":
    main()
