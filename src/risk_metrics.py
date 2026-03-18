#Import libraries
import pandas as pd
import numpy as np
from src.data_loader import collect_price_data

#define function to calculate returns. Log used to get it in equal scale
def calculate_log_returns(prices):
    log_returns = np.log(prices / prices.shift(1)) #shift to get the prior days data
    return log_returns

#define fuction to calculate volatility (annualized)
def calculate_volatility(log_returns):
    volatility = log_returns.std() * np.sqrt(252) #252 for the number of trading days
    return volatility
    
#define function to calculate VaR (value at risk) with 95% confidence using historical data
def calculate_var_95(log_returns, weights):
    portfolio_returns = (log_returns * weights).sum(axis=1) #sum for total return
    var = np.percentile(portfolio_returns.dropna(), 5) #5 represents 5th percentile (worst 5%), drops NaN values
    return var

#define function to calculate sharpe (portfolio return - risk free rate) / volatility
def calculate_sharpe(log_returns, volatility, weights, risk_free_rate):
    portfolio_returns = (log_returns * weights).sum(axis=1) #sum for total return
    annual_return = portfolio_returns.mean() * 252
    sharpe = (annual_return - risk_free_rate) / volatility
    return sharpe
