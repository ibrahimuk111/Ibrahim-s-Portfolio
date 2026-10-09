"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Multi_Modal_Assistant_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.agent_core import MultiModalAgent

def main():
    st.set_page_config(page_title="Multi-Modal Assistant", page_icon="ðŸ¤–", layout="wide")
    st.title("ðŸ¤– Multi-Modal Assistant Agent")
    st.caption("Voice + Image + Text Processing | Author: Muhammad Ibrahim")

    if "agent" not in st.session_state:
        st.session_state.agent = MultiModalAgent()

    agent = st.session_state.agent
    tab1, tab2, tab3 = st.tabs(["ðŸ’¬ Text", "ðŸ–¼ï¸ Image", "ðŸŽ¤ Voice"])

    with tab1:
        text_input = st.text_input("Ask anything")
        if st.button("Send", key="text_btn"):
            if text_input:
                response = agent.process_text(text_input)
                st.success(response)

    with tab2:
        uploaded = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
        img_question = st.text_input("Question about the image")
        if st.button("Analyze", key="img_btn") and uploaded:
            result = agent.process_image(uploaded.read(), img_question)
            st.write(f"**Description:** {result.description}")
            st.metric("Confidence", f"{result.confidence:.0%}")

    with tab3:
        audio = st.file_uploader("Upload Audio", type=["wav", "mp3"])
        if st.button("Transcribe", key="voice_btn") and audio:
            response = agent.process_voice(audio.read())
            st.success(response)

    with st.sidebar:
        st.subheader("Conversation History")
        for msg in agent.get_history():
            st.markdown(f"**{msg['role']}:** {msg['content']}")
        if st.button("Clear History"):
            agent.clear_history()

if __name__ == "__main__":
    main()
