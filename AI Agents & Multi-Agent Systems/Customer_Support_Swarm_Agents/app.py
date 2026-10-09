"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer_Support_Swarm_Agents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

﻿"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Customer_Support_Swarm_Agents
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.swarm_controller import SwarmController

def main():
    st.set_page_config(page_title="Customer Support Swarm", page_icon="ðŸ", layout="wide")
    st.title("ðŸ Customer Support Swarm Agents")
    st.caption("Intelligent Query Routing | Author: Muhammad Ibrahim")

    if "controller" not in st.session_state:
        st.session_state.controller = SwarmController()

    controller = st.session_state.controller
    query = st.text_input("Customer Query", placeholder="e.g., I need a refund for my last payment")

    if st.button("ðŸŽ¯ Route & Respond", type="primary") and query:
        result = controller.handle_query(query)
        r = result["routing"]
        col1, col2 = st.columns(2)
        col1.metric("Routed To", r["domain"].title())
        col2.metric("Confidence", f"{r['confidence']:.0%}")
        st.info(result["response"]["message"])
        st.write("**Suggested Actions:**")
        for action in result["response"]["actions"]:
            st.button(action, disabled=True, key=action)

    with st.sidebar:
        st.subheader("Analytics")
        analytics = controller.get_analytics()
        st.metric("Total Queries", analytics.get("total", 0))
        if analytics.get("domains"):
            st.json(analytics["domains"])

if __name__ == "__main__":
    main()
