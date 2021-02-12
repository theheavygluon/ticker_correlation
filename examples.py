from ticker_correlation import *


#Correlation Between $BB (Blackberry) and $BA (Boeing Airlines). We shouldn't expect a high correlation
correlation('BA', 'BB')

#Spearman Correlation of $RIOT (Riot)and $MARA (Marathon) from Jan 1, 2020 to today, we should expect a very high correlation
correlation('MARA','RIOT', startDate='2020-01-01', endDate=today, corrType='spearman')


#Plot $SPY (SP500 ETF) and $GOOG (GOOGLE)
plot_tickers('SPY','GOOG')

#Print out $GOOG (Google) and $AAPL (Apple) data in a table 
print_datasets('GOOG', 'AAPL', startDate='2021-01-28', endDate='2021-02-12')