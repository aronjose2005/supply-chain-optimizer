import pytest
from src.supply_chain_optimizer import optimize_supply_chain

def test_optimize_supply_chain():
    strategy = optimize_supply_chain(demand_forecast=1200, current_inventory=800)
    assert isinstance(strategy, str)
    assert len(strategy) > 0
