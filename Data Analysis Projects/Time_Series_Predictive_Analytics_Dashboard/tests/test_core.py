"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Time_Series_Predictive_Analytics_Dashboard
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.forecasting import TimeSeriesForecaster

def test_forecasting():
    f = TimeSeriesForecaster()
    res = f.generate_forecast(14)
    assert len(res["forecast_values"]) == 14
