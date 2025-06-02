from supply_chain_optimizer import optimize_supply_chain
from quantum_security import encrypt_data
from demand_forecasting import fetch_market_trends, forecast_demand

def main():
    # Fetch and analyze market trends for demand forecasting
    trends_text = fetch_market_trends()
    print(f"Market Trends: {trends_text}")
    demand_forecast = forecast_demand(trends_text)
    print(f"Demand Forecast: {demand_forecast} units")

    # Optimize supply chain
    current_inventory = 800  # Placeholder
    strategy = optimize_supply_chain(demand_forecast, current_inventory)
    print(f"Supply Chain Optimization Strategy: {strategy}")

    # Quantum-secured data encryption
    data_to_encrypt = f"Demand: {demand_forecast}, Strategy: {strategy}".encode('utf-8')
    encrypted_data = encrypt_data(data_to_encrypt)
    print(f"Encrypted Data: {encrypted_data}")

if __name__ == "__main__":
    main()
