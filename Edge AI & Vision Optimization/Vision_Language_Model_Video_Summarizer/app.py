"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Vision_Language_Model_Video_Summarizer
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.vlm_summarizer import VLMVideoSummarizer

def main():
    st.set_page_config(page_title="VLM Video Summarizer", page_icon="🎥")
    st.title("🎥 Vision-Language Model (VLM) Video Log Summarizer")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    vlm = VLMVideoSummarizer()
    vid = st.text_input("Video File Name", "cctv_log_20261009.mp4")
    
    if st.button("Generate VLM Video Summary"):
        res = vlm.summarize_video_events(vid)
        st.subheader("Summary")
        st.write(res["overall_summary"])
        st.subheader("Timeline Events")
        st.table(res["keyframe_summaries"])

if __name__ == "__main__":
    main()
