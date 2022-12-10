import pandas as pd
from nsepy import get_history
from datetime import date, timedelta
import shelve

def stock():
    s = shelve.open('.\shelve_data\stock_list.db')
    sectoral_list = {}
    for i in s:
        # print(i)
        # print(s[i])
        sectoral_list[i]=s[i]
        # print(sectoral_list)
    s.close()
    return sectoral_list
t=stock()
print(t)


for tick,tker in t.items():
    dict_top_gainers = {}
    list_top_gainers = []
    print(tick)
    for ticker in tker:
        try:
            # print(ticker)
            count = 0
            end_day = date.today()
            start_day = end_day - timedelta(1)
            df = get_history(symbol=ticker, start=start_day, end=end_day)
            data=df[['Open', 'High', 'Low', 'Close', 'Volume']]
            profit = round((data.iloc[-1]["Close"])-(data.iloc[1]["Close"]),2)
            profit_per = round((profit/(data.iloc[-1]["Close"]))*100,2)
            dict_top_gainers['stock']=ticker
            dict_top_gainers['gain/loss']=profit
            dict_top_gainers['gain_loss_per']=profit_per
            list_top_gainers.append(dict_top_gainers)
            dict_top_gainers = {}
        except IndexError as error:
            print("just chill")

    df2=pd.DataFrame.from_dict(list_top_gainers)
    # print(df2)
    # print(df2.sort_values(ascending=False))
    # print(df2.loc[df2.gain_loss_per.idxmax()])
    print(df2.sort_values(by='gain_loss_per', ascending=False).head(5))
    print(df2.sort_values(by='gain_loss_per', ascending=True).head(5))


