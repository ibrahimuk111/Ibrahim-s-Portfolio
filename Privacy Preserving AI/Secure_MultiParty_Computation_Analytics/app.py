"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Secure_MultiParty_Computation_Analytics
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.smpc import SMPCAnalytics

def main():
    st.set_page_config(page_title="SMPC Analytics", page_icon="🔐")
    st.title("🔐 Secure Multi-Party Computation (SMPC) Analytics")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    smpc = SMPCAnalytics()
    st.subheader("Simulate 3 Secret Parties")
    p1 = st.number_input("Party 1 Secret Value", value=50.0)
    p2 = st.number_input("Party 2 Secret Value", value=75.0)
    p3 = st.number_input("Party 3 Secret Value", value=100.0)
    
    if st.button("Compute Joint Analytics Privately"):
        res = smpc.secret_share_mean([p1, p2, p3])
        st.json(res)

if __name__ == "__main__":
    main()
