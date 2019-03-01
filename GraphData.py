
# coding: utf-8

# In[30]:

from pandas_datareader import data
import pandas as pd
import datetime as dt


tickers = ['^NDX']


# In[31]:

todayDate = dt.date.today()
today = "" + str(todayDate.year) + "-" + str(todayDate.month) + "-" + str(todayDate.day)




#Start date set to 30 days before today

startDate = dt.date.today() - dt.timedelta(days=80)
start = "" + str(startDate.year) + "-" + str(startDate.month) + "-" + str(startDate.day)


#pull data from yahoo finance

panel_data = data.DataReader(tickers,'yahoo', start, today)
closing_prices = pd.DataFrame()


# In[32]:

for ticker in tickers:
    ticker_table = panel_data['Adj Close'][ticker]
    closing_prices[ticker] = ticker_table


# In[ ]:




# In[18]:




# In[ ]:




# In[ ]:



