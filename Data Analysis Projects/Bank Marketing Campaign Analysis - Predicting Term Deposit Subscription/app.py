"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Bank Marketing Campaign Analysis - Predicting Term Deposit Subscription
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.core import BankMarketingCampaignAnalysis_Engine

def main():
    st.set_page_config(page_title="Bank Marketing Campaign Analysis - Predicting Term Deposit Subscription", page_icon="🚀")
    st.title("🚀 Bank Marketing Campaign Analysis - Predicting Term Deposit Subscription")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    engine = BankMarketingCampaignAnalysis_Engine()
    inp = st.text_input("Input Parameter", "Default Sample Input")
    
    if st.button("Execute Pipeline"):
        res = engine.process(inp)
        st.json(res)

if __name__ == "__main__":
    main()
