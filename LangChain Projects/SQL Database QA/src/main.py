"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: SQL Database QA
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)






