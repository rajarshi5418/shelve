import pandas as pd

def nifty_index():
    df = pd.read_csv(r'D:\trading\nifty list\All_INDICES2.csv')
    nfty_index = df["INDEXX"].tolist()
    print(nfty_index)
    return nfty_index

nifty_index()