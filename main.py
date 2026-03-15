#load data from the data loader and risk files
from src.data_loader import collect_price_data
from src.risk_metrics import calculate_log_returns, calculate_volatility, calculate_var_95, calculate_sharpe
from src.monte_carlo import run_monte_carlo, plot_monte_carlo
from src.stress_test import run_stress_test, plot_stress_test

#Identify variables
tickers = ["SPY", "QQQ", "AAPL"]
weights = [0.40, 0.40, 0.20] #respective ticker weights of portfolio
risk_free_rate = 0.045
start = "2025-01-01"
end = "2026-01-01"

#Run price data function
data = collect_price_data(tickers, start, end)
historical_data = collect_price_data(tickers, "2007-01-01", "2023-01-01") #Pulls long term data for stress test
print("--- Price Data ---")
print (data.head())

#Run risk analysis function
log_returns = calculate_log_returns(data)
log_returns = log_returns.dropna() #get rid of NaNs
print("--- Risk Analysis ---")
print (log_returns.head())

#Run volatility analysis function
volatility = calculate_volatility(log_returns)
print("--- Annualized Volatility ---")
print(volatility.to_string())

#Run VaR analysis function
VaR = calculate_var_95(log_returns, weights)
print("--- VaR 95% Confidence ---")
print(VaR)

#Run Sharpe calculation function
sharpe = calculate_sharpe(log_returns, volatility.mean(), weights, risk_free_rate)
print ("--- Sharpe ---")
print(sharpe)

#Run plot functions
results = run_monte_carlo(log_returns, weights, 10000, 252)
plot_monte_carlo(results, tickers)

#Stress tests

# 2008 Financial Crisis
cr1 = run_stress_test(historical_data, "2008-09-01", "2009-03-31", "2008 Financial Crisis")
plot_stress_test(cr1, "2008 Financial Crisis")

# COVID Crash
cr2 = run_stress_test(historical_data, "2020-02-01", "2020-03-31", "COVID Crash")
plot_stress_test(cr2, "COVID Crash")

# 2022 Rate Hike Selloff
cr3 = run_stress_test(historical_data, "2022-01-01", "2022-12-31", "2022 Rate Hike Selloff")
plot_stress_test(cr3, "2022 Rate Hike Selloff")



