"""
Methods related to cryptocurrency data
    - get latest data
    - perform data cleaning
"""

import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

time_period = '60d'
price_intervals = '1d'


def plot_data():
    """
    Function takes the bitcoin price data from last 20 Days
    plots a graph: Date, Price relation
    And saves the plot as image in assets (overrides existing)
    """
    print("m called")
    data = yf.download(tickers='BTC-USD', period=time_period,
                       interval=price_intervals)  # coin value for last 3 days at 0000
    # df = pd.DataFrame({'lab': data['Adj Close'], 'val': data['Adj Close']})
    # ax = df.plot.bar(x='lab', y='val', rot=0)
    x = ["".join(str(date_time).split()[0]) for date_time in data['Adj Close'].index]  # x axis for graph
    y = [float(price) for price in data['Adj Close']]
    relation = pd.DataFrame({'date': x, 'BTC_price': y})
    relation.plot('date', 'BTC_price', marker='o', color='b')
    plt.xticks(rotation=0)
    plt.show()


def get_data(currency_name):
    """
    Function takes param: BTC-USD | ETH-USD
    return real time data for price
    """
    data = yf.download(tickers=currency_name, period=time_period, interval=price_intervals)  #
    # coin value for  last 3 days at 0000
    price = [float(price) for price in data['Adj Close']]
    return price


if __name__ == '__main__':
    plot_data()
