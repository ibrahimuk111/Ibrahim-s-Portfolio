"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: VLM_Video_QA_Summarizer
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.vlm_video_qa import VLMVideoQA

def main():
    st.set_page_config(page_title="VLM Video QA", page_icon="🎥")
    st.title("🎥 VLM Video QA & Scene Summarizer (Qwen2-VL)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    qa = VLMVideoQA()
    vid = st.text_input("Video File", "traffic_surveillance.mp4")
    q = st.text_input("Question", "What color car entered the intersection at 00:15?")
    
    if st.button("Run VLM QA"):
        res = qa.answer_video_question(vid, q)
        st.info(res["vlm_answer"])
        st.json(res)

if __name__ == "__main__":
    main()
