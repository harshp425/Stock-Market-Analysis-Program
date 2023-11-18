import pandas as pd
import yahoo_scraper
import matplotlib.pyplot as plt
from used_functions import make_num
from used_functions import dictionary_keys
import plotly.graph_objects as go
import numpy as np


def analysis1(symbol, key):
    data = yahoo_scraper.valuation_measures(symbol, key)[0]
    data.reverse()
    data2 = []
    for x in range(len(data)):
        data2 = data2 + [make_num(data[x])]
    data_dict = {dictionary_keys[key]: data2}
    data_dates = ['3/31/2022','6/30/2022', '9/30/2022', '12/31/2022', '3/31/2023', '4/27/2023']
    v = yahoo_scraper.valuation_measures(symbol, key)[1]
    if type(v)==int:
        data_dates.remove(data_dates[v])
    df = pd.DataFrame(data=data_dict, index=data_dates)
    df[dictionary_keys[key]] = df[dictionary_keys[key]].astype(float)
    print(df)
    df.plot(use_index=True, grid=True, figsize=(15,7))

    plt.legend()
    plt.title(symbol+' '+dictionary_keys[key])
    plt.xlabel('Dates')
    plt.ylabel(dictionary_keys[key])
    plt.show()

    return df

def historical_analysis(symbol,key, arg):

    Dictionary = {}
    for x in key:
        Dictionary[x] = yahoo_scraper.historical_data(symbol, x)
    Dictionary['Date'] = yahoo_scraper.historical_data(symbol, 'Date')
   
    df = pd.DataFrame.from_dict(data = Dictionary)
    df['Date'] = pd.to_datetime(df['Date'])
    new_df = df.set_index('Date', inplace=False)

    for x in key:
        new_df[x] = new_df[x].astype(float)


    if arg == "1":
        fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (19,7))
        new_df['Open'].plot(ax = axes[0])
        new_df['High'].plot(ax = axes[0])
        new_df['Low'].plot(ax = axes[0])
        new_df['Close'].plot(ax = axes[0])
        new_df['Volume'].plot(ax = axes[1])

        axes[0].set_title(f'{symbol} Open, High, Low, and Close Prices')
        axes[0].legend()
        axes[0].set_xlabel('Dates')
        axes[0].set_ylabel('Price')
        axes[1].set_title(f'{symbol} Volume')
        axes[1].legend()
        axes[1].set_xlabel('Dates')
        axes[1].set_ylabel('Volume of Traders')

        plt.show()

    if arg == "2":
        plt.style.use('fivethirtyeight')
        new_df['Open'].plot()
        plt.title(f'{symbol} Open Price')
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('Open Price')         
        plt.show()

    if arg == "3":
        plt.style.use('fivethirtyeight')
        new_df['Close'].plot()
        plt.title(f'{symbol} Close Price')
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('Close Price')         
        plt.show()

    if arg == "4":
        plt.style.use('fivethirtyeight')
        new_df['High'].plot()
        plt.title(f'{symbol} High Price')
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('High Price')         
        plt.show()

    if arg == "5":
        plt.style.use('fivethirtyeight')
        new_df['Low'].plot()
        plt.title(f'{symbol} Low Price')
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('Low Price')         
        plt.show()

    if arg == "6":
        plt.style.use('fivethirtyeight')
        new_df['Volume'].plot()
        plt.title(f'{symbol} Volume Price')
        plt.legend()
        plt.xlabel('Dates')
        plt.ylabel('Volume Price')         
        plt.show()

    if arg == "7":
       fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])
       fig.show()

    if arg == "8":
        plt.style.use('fivethirtyeight')
        new_df['SMA5'] = new_df['Close'].rolling(window=5).mean()
        new_df['SMA15'] = new_df['Close'].rolling(window=15).mean()
        new_df['Signal'] = np.where(new_df['SMA5']>new_df['SMA15'], 1, 0)
        new_df['Position'] = new_df['Signal'].diff()

        new_df['Buy'] = np.where(new_df['Position']==1,new_df['Close'],np.NAN)
        new_df['Sell'] = np.where(new_df['Position']==-1,new_df['Close'],np.NAN)

        plt.figure(figsize=(16,8))
        plt.title('Close Price History with Buy and Sell Signals')
        plt.plot(new_df['Close'], alpha = 0.5, label = "Close")
        plt.plot(new_df['SMA5'], alpha = 0.5, label = "SMA5")
        plt.plot(new_df['SMA15'], alpha = 0.5, label = "SMA15")
        plt.legend()
        #plt.scatter(new_df.index, new_df['Buy'], alpha = 1, label = "Buy Signal", marker = "^", color = 'green')
        #plt.scatter(new_df.index, new_df['Sell'], alpha = 1, label = "Sell Signal", marker = "v", color = 'red')


        plt.xlabel('Dates')
        plt.ylabel('Close Price')
        plt.show()

   
