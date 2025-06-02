import pytest
from src.demand_forecasting import forecast_demand

def test_forecast_demand():
    demand = forecast_demand("Positive market trends for electronics.")
    assert 0 <= demand <= 1000  # Based on simplified scaling in forecast_demand
