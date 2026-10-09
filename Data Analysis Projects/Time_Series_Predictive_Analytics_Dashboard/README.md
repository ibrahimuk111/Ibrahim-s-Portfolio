# Time_Series_Predictive_Analytics_Dashboard

Predictive time-series forecasting dashboard with trend/seasonality decomposition, Prophet modeling, and confidence interval estimation.

## System Architecture

```mermaid
graph LR
    HistData[Historical Time Series Data] --> Decompose[Trend & Seasonality Decomposition]
    Decompose --> ProphetModel[Prophet / NeuralProphet Engine]
    ProphetModel --> Interval[Confidence Interval Calculation]
    Interval --> Dashboard[Interactive Forecasting Line Chart]

```

## Directory Structure

```
Time_Series_Predictive_Analytics_Dashboard/
├── src/           # Core modules
├── tests/         # Unit tests (pytest)
├── app.py         # Application entry point
├── Dockerfile     # Container configuration
├── requirements.txt
└── LICENSE
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
python app.py

# Run tests
pytest tests/ -v

# Container build
docker build -t time_series_predictive_analytics_dashboard .
docker run -p 8000:8000 time_series_predictive_analytics_dashboard
```


---

## Author & Licensing

**Author:** Muhammad Ibrahim  
**Email:** [ukibrahim111@gmail.com](mailto:ukibrahim111@gmail.com)  
**GitHub:** [https://github.com/ibrahimuk111](https://github.com/ibrahimuk111)  
**License:** MIT License - Copyright (c) 2026 Muhammad Ibrahim

If you find this project useful, please consider giving it a star and connecting with me for collaborations.

