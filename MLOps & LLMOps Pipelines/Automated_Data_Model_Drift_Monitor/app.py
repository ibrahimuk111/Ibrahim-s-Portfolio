"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Automated_Data_Model_Drift_Monitor
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
import numpy as np
from src.drift_detector import DriftMonitor

def main():
    st.set_page_config(page_title="Data & Model Drift Monitor", page_icon="📈")
    st.title("📈 Automated Data & Model Drift Monitor")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    monitor = DriftMonitor()
    
    st.sidebar.header("Data Distribution Shift")
    shift = st.sidebar.slider("Mean Shift Delta", 0.0, 3.0, 0.5, 0.1)
    
    ref = np.random.normal(10, 2, 1000).tolist()
    curr = np.random.normal(10 + shift, 2, 1000).tolist()
    
    res = monitor.calculate_ks_drift(ref, curr)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Drift Score", res["drift_score"])
    col2.metric("Status", res["status"])
    col3.metric("Is Drifted", str(res["is_drifted"]))

if __name__ == "__main__":
    main()
