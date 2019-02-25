
# coding: utf-8

#To Do: push the daily portfolio dataframe into the database so that users may see which equities
# their stocks are allocated in

from pandas_datareader import data
import pandas as pd
import datetime as dt
from app import db
from models import *


#Declare the tickers here that you hope to include

tickers = ['AAL','AAPL','ADBE','ADI','ADP','ADSK','ALGN','ALXN','AMAT',
           'AMD','AMGN','AMZN','ASML','ATVI','AVGO','BIDU','BIIB',
           'BKNG','BMRN','CDNS','CELG','CERN','CHKP','CHTR','CMCSA',
           'COST','CSX','CTAS','CTRP','CTSH','CTXS','DLTR','EA',
           'EBAY','EXPE','FAST','FB','FISV','FOX','GILD','GOOG','HAS',
           'HSIC','IDXX','ILMN','INCY','INTC','INTU','ISRG','JBHT',
           'JD','KHC','KLAC','LBTYA','LRCX','LULU','MAR','MCHP','MDLZ',
           'MELI','MNST','MSFT','MU','MXIM','MYL','NFLX','NTAP','NTES',
           'NVDA','NXPI','ORLY','PAYX','PCAR','PEP','PYPL','QCOM','REGN',
           'ROST','SBUX','SIRI','SNPS','SWKS','SYMC','TMUS','TSLA','TTWO',
           'TXN','UAL','ULTA','VRSK','VRSN','VRTX','WBA','WDAY','WDC',
           'WLTW','WYNN','XEL','XLNX'
          ]







#will be pulled form database


#End date set to today's date


todayDate = dt.date.today() - dt.timedelta(days=3)
today = "" + str(todayDate.year) + "-" + str(todayDate.month) + "-" + str(todayDate.day)




#Start date set to 80 days before today

startDate = dt.date.today() - dt.timedelta(days=80) - dt.timedelta(days=3)
start = "" + str(startDate.year) + "-" + str(startDate.month) + "-" + str(startDate.day)


#pull data from yahoo finance

panel_data = data.DataReader(tickers,'yahoo', start, today)
closing_prices = pd.DataFrame()
#closing_prices.to_csv('closing_prices.csv')

# for user in database:
# total_capital = user.getBalance()
users = User.query.all()
for user in users:
    total_capital = user.balance



    for ticker in tickers:
        ticker_table = panel_data['Adj Close'][ticker]
        closing_prices[ticker] = ticker_table



    for j in range(2,-1,-1):

        #Construct a list of 40 day moving average

        moving_avg_40_lst = []

        for ticker in tickers:
            if j == 1:
                moving_avg_40 = closing_prices[ticker][-40-j:-1*j].sum() / len(closing_prices[ticker][-40-j:-1*j])
                moving_avg_40_lst.append(moving_avg_40)
            else:
                moving_avg_40 = closing_prices[ticker][-40:].sum() / len(closing_prices[ticker][-40:])
                moving_avg_40_lst.append(moving_avg_40)



        #Construct a list of 5 day moving average

        moving_avg_5_lst = []

        for ticker in tickers:
            if j == 1:
                moving_avg_5 = closing_prices[ticker][-5-j:-1*j].sum() / len(closing_prices[ticker][-5-j:-1*j])
                moving_avg_5_lst.append(moving_avg_5)
            else:
                moving_avg_5 = closing_prices[ticker][-5:].sum() / len(closing_prices[ticker][-5:])
                moving_avg_5_lst.append(moving_avg_5)



        #Construct data frame that hold 40 and 5 day moving averages

        moving_avg = pd.DataFrame()
        moving_avg['ticker'] = tickers
        moving_avg['moving_avg_40'] = moving_avg_40_lst
        moving_avg['moving_avg_5'] = moving_avg_5_lst
        moving_avg = moving_avg.set_index('ticker')





        short_term_up = []

        for ticker in moving_avg.index:
            if(moving_avg['moving_avg_40'][ticker] < moving_avg['moving_avg_5'][ticker]):
                short_term_up.append(1)
            else:
                short_term_up.append(0)



        #Create row of delta between 40 and 5 day moving average

        short_term_delta_percent = []
        short_term_delta = []
        i = 0
        k = 0

        for ticker in moving_avg.index:
            i = (moving_avg['moving_avg_5'][ticker] - moving_avg['moving_avg_40'][ticker])/moving_avg['moving_avg_40'][ticker]
            k = (moving_avg['moving_avg_5'][ticker] - moving_avg['moving_avg_40'][ticker])
            short_term_delta_percent.append(i)
            short_term_delta.append(k)

        moving_avg['short_term_up'] = short_term_up
        moving_avg['short_term_delta_percent'] = short_term_delta_percent
        moving_avg['short_term_delta'] = short_term_delta



        #Setting a delta threshhold, this will determine the buy/sell threshold
        # +threshold will initiate a buy
        # -threshold will initiate a sell

        threshold = .0

        #every basis point above the threshold will determine the basis
        # points of the stock to be bought/sold


        #Declaring list of buy/sell stock to be inserted into DataFrame

        buy_ticker = []
        buy_delta = []

        #sell_ticker = []
        #sell_delta = []


        for ticker in moving_avg.index:
            delta = moving_avg['short_term_delta'][ticker]
            
            #if delta > threshold:
            buy_ticker.append(ticker)
            buy_delta.append(delta)
        
            #elif delta < -1*threshold:
    #            sell_ticker.append(ticker)
    #            sell_delta.append(delta)



        # In[52]:

        today_buy = pd.DataFrame()
        today_buy['ticker'] = buy_ticker
        today_buy['delta'] = buy_delta

        #today_sell = pd.DataFrame()
        #today_sell['ticker'] = sell_ticker
        #today_sell['delta'] = sell_delta

        today_buy = today_buy.sort_values('delta', ascending=False)
        #today_sell = today_sell.sort_values('delta')

        today_buy = today_buy.set_index('ticker')
        #today_sell = today_sell.set_index('ticker')





        if j == 2:
            yesterday_buy = today_buy


            #today_sell_delta = today_sell

        else:
            buy_change = []
            buy_change_percent = []
            #sell_change = []

            for ticker in yesterday_buy.index:
                change = today_buy['delta'][ticker] - yesterday_buy['delta'][ticker]
                change_percent = change / yesterday_buy['delta'][ticker]
                buy_change.append(change)
                buy_change_percent.append(change_percent)


            daily_change = pd.DataFrame()
            daily_change['ticker'] = yesterday_buy.index
            daily_change['daily_change'] = buy_change
            daily_change['daily_change_percent'] = buy_change_percent

            daily_change = daily_change.sort_values('daily_change', ascending=False)
            daily_change = daily_change.set_index('ticker')

            #print(yesterday_buy)
            #print(today_buy)
            #print(daily_change)

            yesterday_buy = today_buy



            #re-investing money in stocks
            counter = 0
            portfolio_stocks = []
            portfolio_weight = []
            portfolio_amt = []
            portfolio_buy_price = []
            for ticker in daily_change.index:
                if counter < 10:
                    if (daily_change['daily_change'][ticker] > 0 and daily_change['daily_change_percent'][ticker] > 0):
                        portfolio_stocks.append(ticker)
                        portfolio_weight.append(daily_change['daily_change'][ticker])
                        portfolio_buy_price.append(closing_prices[ticker][-j-1])
                        counter += 1


            #initial portfolio investment
            if (j == 1):
                counter = 0
                portfolio = pd.DataFrame()
                for ticker in portfolio_stocks:
                    amt = (portfolio_weight[counter] / sum(portfolio_weight)) * total_capital
                    portfolio_amt.append(amt)
                    counter += 1

                portfolio['ticker'] = portfolio_stocks
                portfolio['amt'] = portfolio_amt
                portfolio['price'] = portfolio_buy_price

                portfolio = portfolio.set_index('ticker')

            else:
                for ticker in portfolio.index:
                    volume = portfolio['amt'][ticker] / portfolio['price'][ticker]
                    made = (closing_prices[ticker][-1] - portfolio['price'][ticker]) * volume

                    beta_score = -made
                    
                    if (beta_score < 1):
                        total_capital = total_capital - beta_score


                counter = 0
                portfolio = pd.DataFrame()
                for ticker in portfolio_stocks:
                    amt = (portfolio_weight[counter] / sum(portfolio_weight)) * total_capital
                    portfolio_amt.append(amt)
                    counter += 1
                
                portfolio['ticker'] = portfolio_stocks
                portfolio['amt'] = portfolio_amt
                portfolio['price'] = portfolio_buy_price

                portfolio = portfolio.set_index('ticker')


            

    user.balance = total_capital
    db.session.commit()

    #push total_capital back to user.balance
    #To Do LATER: push portfolio to database, replacing the portfolio thats currently there
            
                









