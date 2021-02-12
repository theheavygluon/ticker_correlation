from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
from matplotlib import pyplot as plt 
import pandas as pd
import numpy as np
from datetime import datetime
from scipy.stats import pearsonr
from scipy.stats import spearmanr 
from matplotlib import pyplot as plt 

today = str(datetime.now().strftime('%Y-%m-%d'))
def print_datasets(ticker1, ticker2, startDate='2020-01-01', endDate=today):
    dataset1 = data.DataReader(ticker1,'yahoo',startDate,endDate)
    dataset2 = data.DataReader(ticker2,'yahoo',startDate,endDate)
    return print(ticker1 + ": ", dataset1),print(ticker2 + ": ",dataset2)

def price2change(dataset, type='daily'):
    if type.lower() == "daily":
        masterlist = []
        i = 0
        while i<=11:
            small = [100 * (b - a) / a for a, b in zip(dataset[i][::1], dataset[i][1::1])]
            masterlist.append(small)
            i+=1
    if type.lower() == "total":
        masterlist = []
        i = 0
        while i<=11:
            small = [100 * (b - dataset[i][0]) / dataset[i][0] for b in zip(dataset[i][1::1])]
            masterlist.append(small)
            i+=1
    return masterlist




def get_datasets(ticker1, ticker2, startDate='2020-01-01', endDate=str(datetime.now().strftime('%Y-%m-%d'))):
    dataset1 = np.array(data.DataReader(ticker1,'yahoo',startDate,endDate))
    dataset2 = np.array(data.DataReader(ticker2,'yahoo',startDate,endDate))
    h1 = np.array(dataset1[:,0])
    l1 = np.array(dataset1[:,1])
    o1 = np.array(dataset1[:,2])
    c1 = np.array(dataset1[:,3])
    v1 = np.array(dataset1[:,4])
    ac1 = np.array(dataset1[:,5])
    h2 = np.array(dataset2[:,0])
    l2 = np.array(dataset2[:,1])
    o2 = np.array(dataset2[:,2])
    c2 = np.array(dataset2[:,3])
    v2 = np.array(dataset2[:,4])
    ac2 = np.array(dataset2[:,5])
    return h1,l1,o1,c1,v1,ac1,h2,l2,o2,c2,v2,ac2


def correlation(ticker1, ticker2, startDate='2020-01-01', endDate=str(datetime.now().strftime('%Y-%m-%d')), corrType='pearson'):
    data = get_datasets(ticker1, ticker2, startDate, endDate)
    if corrType.lower() == 'pearson':
        hi_corr = pearsonr(data[0], data[6])
        lo_corr = pearsonr(data[1], data[7])
        o_corr = pearsonr(data[2], data[8])
        cl_corr = pearsonr(data[3], data[9])
        vo_corr = pearsonr(data[4], data[10])
        adj_corr = pearsonr(data[5], data[11])
        print('Hi Correlation: ' + str(hi_corr[0]))
        print('Lo Correlation: ' + str(lo_corr[0]))
        print('Op Correlation: ' + str(o_corr[0]))
        print('Cl Correlation: ' + str(cl_corr[0]))
        print('Vo Correlation: ' + str(vo_corr[0]))
        print('Adj. Cl Correlation: ' + str(adj_corr[0]))
    
    if corrType.lower() == 'spearman':
        hi_corr = spearmanr(data[0], data[6])
        lo_corr = spearmanr(data[1], data[7])
        o_corr = spearmanr(data[2], data[8])
        cl_corr = spearmanr(data[3], data[9])
        vo_corr = spearmanr(data[4], data[10])
        adj_corr = spearmanr(data[5], data[11])
        print('Hi Correlation: ' + str(hi_corr[0]))
        print('Lo Correlation: ' + str(lo_corr[0]))
        print('Op Correlation: ' + str(o_corr[0]))
        print('Cl Correlation: ' + str(cl_corr[0]))
        print('Vo Correlation: ' + str(vo_corr[0]))
        print('Adj. Cl Correlation: ' + str(adj_corr[0]))

    return 
#H-L-O-C-V-Ajd
def plot_tickers(ticker1, ticker2, startDate='2020-01-01', endDate=str(datetime.now().strftime('%Y-%m-%d'))):
    data_price = get_datasets(ticker1, ticker2, startDate, endDate)
    data_change = price2change(data_price)
    data_change_total = price2change(data_price, 'total')
    xvals = [i for i in np.linspace(0,len(data_change[0]),len(data_change[0]))]
    i = 0
    while i <=5:
        if i == 0:
            tit = "Daily Percent Change of " + ticker1 + " and " + ticker2 + " (Hi.)\n from " + startDate + " to " + endDate
        if i == 1:
            tit = "Daily Percent Change of " + ticker1 + " and " + ticker2 + " (Lo.)\n from " + startDate + " to " + endDate
        if i == 2:
            tit = "Daily Percent Change of " + ticker1 + " and " + ticker2 + " (Op.)\n from " + startDate + " to " + endDate
        if i == 3:
            tit = "Daily Percent Change of " + ticker1 + " and " + ticker2 + " (Cl.)\n from " + startDate + " to " + endDate
        if i == 4:
            tit = "Daily Percent Change of " + ticker1 + " and " + ticker2 + " (Vol.)\n from " + startDate + " to " + endDate
        if i == 5:
            tit = "Daily Percent Change of " + ticker1 + " and " + ticker2 + " (Adj. Cl)\n from " + startDate + " to " + endDate

        plt.plot(xvals, data_change[i], color = 'r', label = ticker1)
        plt.plot(xvals, data_change[i+6], color = 'b', label = ticker2)
        plt.title(tit)
        plt.legend()
        plt.xlabel("Number of days since " + startDate)
        plt.ylabel("Change (%)")
        plt.show()
        i+=1
    i = 0
    while i <=5:
        if i == 0:
            tit = "Total Percent Change of " + ticker1 + " and " + ticker2 + " (Hi.)\n from " + startDate + " to " + endDate
        if i == 1:
            tit = "Total Percent Change of " + ticker1 + " and " + ticker2 + " (Lo.)\n from " + startDate + " to " + endDate
        if i == 2:
            tit = "Total Percent Change of " + ticker1 + " and " + ticker2 + " (Op.)\n from " + startDate + " to " + endDate
        if i == 3:
            tit = "Total Percent Change of " + ticker1 + " and " + ticker2 + " (Cl.)\n from " + startDate + " to " + endDate
        if i == 4:
            tit = "Total Percent Change of " + ticker1 + " and " + ticker2 + " (Vol.)\n from " + startDate + " to " + endDate
        if i == 5:
            tit = "Total Percent Change of " + ticker1 + " and " + ticker2 + " (Adj. Cl)\n from " + startDate + " to " + endDate

        plt.plot(xvals, data_change_total[i], color = 'r', label = ticker1)
        plt.plot(xvals, data_change_total[i+6], color = 'b', label = ticker2)
        plt.title(tit)
        plt.legend()
        plt.xlabel("Number of days since " + startDate)
        plt.ylabel("Change (%)")
        plt.show()
        i+=1
        

    



