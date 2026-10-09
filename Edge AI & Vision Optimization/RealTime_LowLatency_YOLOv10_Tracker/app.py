"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RealTime_LowLatency_YOLOv10_Tracker
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.tracker import YOLOTracker

def main():
    st.set_page_config(page_title="YOLOv10 Tracker", page_icon="👁️")
    st.title("👁️ Real-Time Low-Latency YOLOv10 Tracker (TensorRT/ONNX)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    tracker = YOLOTracker()
    if st.button("Simulate Video Stream (10 Frames)"):
        for i in range(10):
            res = tracker.process_frame(i)
            st.write(f"Frame {i}: Inference {res['inference_time_ms']}ms | FPS: {res['fps']} | Detections: {len(res['detections'])}")

if __name__ == "__main__":
    main()
