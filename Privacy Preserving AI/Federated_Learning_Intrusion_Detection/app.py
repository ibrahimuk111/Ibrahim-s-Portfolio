"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Federated_Learning_Intrusion_Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.federated import FederatedServer

def main():
    st.set_page_config(page_title="Federated Learning Intrusion Detection", page_icon="🔒")
    st.title("🔒 Federated Learning Intrusion Detection (Flower Framework)")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    server = FederatedServer()
    st.subheader("Simulate Decentralized Node Client Updates")
    c1 = st.slider("Node 1 Accuracy", 0.5, 1.0, 0.92)
    c2 = st.slider("Node 2 Accuracy", 0.5, 1.0, 0.88)
    c3 = st.slider("Node 3 Accuracy", 0.5, 1.0, 0.95)
    
    if st.button("Aggregate Federated Weights"):
        res = server.aggregate_weights([c1, c2, c3])
        st.success(f"Global Model Aggregated Accuracy: {res['global_aggregated_accuracy']:.0%}")

if __name__ == "__main__":
    main()
