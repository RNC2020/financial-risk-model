#Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

colors = ['blue', 'red', 'green', 'orange', 'purple']

def run_stress_test (prices, start_date, end_date, title):
    crisis_data = prices.loc[start_date:end_date] #.loc filters by date range
    cumulative_return = crisis_data / crisis_data.iloc[0] #.iloc[0] grabs first row as baseline (first days value)
    return cumulative_return

def plot_stress_test (cumulative_return, title):
    for i, column in enumerate(cumulative_return.columns): #enumerate gives index and value
        plt.plot(cumulative_return[column], color = colors[i], label = column)
    plt.title(f'Stress Test: {title}') #f-string to embed variable into string
    plt.xlabel('Date')
    plt.ylabel('Returns')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
