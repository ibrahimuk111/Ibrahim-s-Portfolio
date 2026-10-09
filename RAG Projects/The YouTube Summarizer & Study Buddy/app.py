"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: The YouTube Summarizer & Study Buddy
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import TheYouTubeSummarizer_StudyBuddEngine

def main():
    st.set_page_config(page_title="The YouTube Summarizer & Study Buddy", page_icon="🚀")
    st.title("🚀 The YouTube Summarizer & Study Buddy")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = TheYouTubeSummarizer_StudyBuddEngine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
