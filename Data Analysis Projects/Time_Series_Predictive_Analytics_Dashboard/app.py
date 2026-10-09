"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Time_Series_Predictive_Analytics_Dashboard
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.forecasting import TimeSeriesForecaster

def main():
    st.set_page_config(page_title="Time Series Analytics", page_icon="📈")
    st.title("📈 Time-Series Predictive Analytics Dashboard")
    st.caption("Author: Muhammad Ibrahim | ukibrahim111@gmail.com")
    
    forecaster = TimeSeriesForecaster()
    days = st.slider("Forecast Horizon (Days)", 7, 90, 30)
    
    if st.button("Generate Predictive Forecast"):
        res = forecaster.generate_forecast(days)
        st.line_chart(res["forecast_values"])
        st.metric("Model MAPE Error", f"{res['mape_error']}%")

if __name__ == "__main__":
    main()
