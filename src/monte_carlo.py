#import numpy for math, pandas for dataframes, and matplotlib.pyplot for plotting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Define the monte carlo simulation
def run_monte_carlo(log_returns, weights, simulations, days):
    portfolio_returns = (log_returns * weights).sum(axis = 1)
    volatility = portfolio_returns.std()
    daily_mean = portfolio_returns.mean()

    results = [] #creates empy list to store data

#for loop for simulation iterations
    for i in range (simulations):
        #generates random returns from historical mean and volitility
        daily_returns = np.random.normal(daily_mean, volatility, days)
        #cumulative products of daily returns
        price_path = np.cumprod(1 + daily_returns)
        #ude .append to add the price_path to the bottom of the results data
        results.append(price_path)

    return results


#Define the plot function for the monto carlo
def plot_monte_carlo(results, tickers):
    df = pd.DataFrame(results).T #.T transposes the DataFrame (flips rows/columns)
    plt.plot(df, alpha = 0.1, color = 'blue') #alpha=0.1 to make lines 10% opaque
    plt.title('Monte Carlo 10,000 Simulations')
    plt.xlabel('Days')
    plt.ylabel('Returns')
    plt.show()
    #Add legend to display total and each ticker
              
