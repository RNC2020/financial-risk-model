#Data Loader for Finance Risk Model
#Last Updated: 3/10/26
#Ryan Chen

import yfinance as yf

#Create function to using inputs of ticker, start date, end date. Only return close prices

def collect_price_data(tickers, start, end):
    data = yf.download(tickers, start, end) 
    return data["Close"]
    
