"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Codebasics FAQ Chatbot
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db

st.title("Codebasics Q&A 🌱")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])






