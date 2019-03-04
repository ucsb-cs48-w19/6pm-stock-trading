from pandas_datareader import data
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
#from datetime import datetime
tickers = ['^NDX']


# In[31]:
def graphMaker():
    filePath = 'static/plot.png'
    todayDate = dt.date.today()
    today = "" + str(todayDate.year) + "-" + str(todayDate.month) + "-" + str(todayDate.day)


    # Start date set to 30 days before today

    startDate = dt.date.today() - dt.timedelta(days=40)
    start = "" + str(startDate.year) + "-" + str(startDate.month) + "-" + str(startDate.day)


    # pull data from yahoo finance

    panel_data = data.DataReader(tickers, 'yahoo', start, today)
    closing_prices = pd.DataFrame()
    # print(panel_data['Close'])
    # print(panel_data.info())
    panel_data[['Open', 'Adj Close']].plot(figsize=(15, 5))
    plt.title('Recent 30 Days Stock Trading')
    plt.plot()
    plt.savefig('static/plot.png')
    print('plot saved')
    


    for ticker in tickers:
        # print(ticker)
        ticker_table = panel_data['Adj Close'][ticker]
        closing_prices[ticker] = ticker_table
    return filePath
    # print(ticker_table)
    # print(closing_prices[ticker])


# year = [1960, 1970, 1980, 1990, 2000, 2010]
# pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
# pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
# plt.plot(year, pop_pakistan, color='g')
# plt.plot(year, pop_india, color='orange')
# plt.xlabel('Countries')
# plt.ylabel('Population in million')
# plt.title('Pakistan India Population till 2010')
# plt.show()


# plotly.tools.set_credentials_file(username='DemoAccount', api_key='lr1c37zw81')
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

# trace = go.Ohlc(x=df['Date'],
#                 open=df['AAPL.Open'],
#                 high=df['AAPL.High'],
#                 low=df['AAPL.Low'],
#                 close=df['AAPL.Close'])

# layout = go.Layout(
#     xaxis=dict(
#         rangeslider=dict(
#             visible=False
#         )
#     )
# )

# data = [trace]

# fig = go.Figure(data=data, layout=layout)
# py.iplot(fig, filename='simple_candlestick')
if __name__== "__main__":
    graphMaker()
