import pandas as pd
import shelve

s = shelve.open('.\shelve_data\stock_list.db')

def nifty():
    df = pd.read_csv(r'nifty.csv')
    nfty = df["NIFTY 50"].tolist()
    s['NIFTY50'] = nfty
    return nfty

nifty()

def nifty_auto():
    df = pd.read_csv(r'NIFTY_AUTO.csv')
    nfty_auto = df["NIFTY_AUTO"].tolist()
    s['nfty_auto']=nfty_auto
    # print(nfty_auto)
    return nfty_auto

nifty_auto()

def nifty_bank():
    df = pd.read_csv(r'NIFTY_BANK.csv')
    nfty_bnk = df["NIFTY_BANK"].tolist()
    s['nfty_bnk'] = nfty_bnk
    # print(nfty_bnk)
    return nfty_bnk

nifty_bank()

def nifty_consumer_durables():
    df = pd.read_csv(r'NIFTY_CONSUMER_DURABLES.csv')
    nfty_consumer_durables = df["NIFTY_CONSUMER_DURABLES"].tolist()
    s['nfty_consumer_durables'] = nfty_consumer_durables
    print(nfty_consumer_durables)
    return nfty_consumer_durables

nifty_consumer_durables()

def nifty_energy():
    df = pd.read_csv(r'NIFTY_AUTO.csv')
    nfty_energy = df["NIFTY_AUTO"].tolist()
    s['nfty_energy'] = nfty_energy
    # print(nfty_energy)
    return nfty_energy

nifty_energy()

def nifty_financial_service():
    df = pd.read_csv(r'NIFTY_FINANCIAL_SERVICES.csv')
    nfty_fin_srv = df["NIFTY_FINANCIAL_SERVICES"].tolist()
    s['nfty_fin_srv'] = nfty_fin_srv
    # print(nfty_fin_srv)
    return nfty_fin_srv

nifty_financial_service()

def nifty_fmcg():
    df = pd.read_csv(r'NIFTY_FMCG.csv')
    nfty_fmcg = df["NIFTY_FMCG"].tolist()
    s['nfty_fmcg'] = nfty_fmcg
    print("fmcg",nfty_fmcg)
    return nfty_fmcg

nifty_fmcg()

def nifty_healthcare():
    df = pd.read_csv(r'NIFTY_HEALTHCARE.csv')
    nfty_healthcare = df["NIFTY_HEALTHCARE"].tolist()
    s['nfty_healthcare'] = nfty_healthcare
    # print(nfty_healthcare)
    return nfty_healthcare

nifty_healthcare()


def nifty_it():
    df = pd.read_csv(r'NIFTY_IT.csv')
    nfty_it = df["NIFTY_IT"].tolist()
    s['nfty_it'] = nfty_it
    # print(nfty_it)
    return nfty_it

nifty_it()

def nifty_media():
    df = pd.read_csv(r'NIFTY_MEDIA.csv')
    nfty_media = df["NIFTY_MEDIA"].tolist()
    s['nfty_media'] = nfty_media
    print("media",nfty_media)
    return nfty_media

nifty_media()

def nifty_metal():
    df = pd.read_csv(r'NIFTY_METAL.csv')
    nfty_metal = df["NIFTY_METAL"].tolist()
    s['nfty_metal'] = nfty_metal
    # print(nfty_metal)
    return nfty_metal

nifty_metal()

def nifty_midcap_50():
    df = pd.read_csv(r'NIFTY_MIDCAP_50.csv')
    nfty_mdcp_50 = df["NIFTY_MIDCAP_50"].tolist()
    s['nfty_mdcp_50'] = nfty_mdcp_50
    # print(nfty_mdcp_50)
    return nfty_mdcp_50

nifty_midcap_50()

def nifty_midcap_100():
    df = pd.read_csv(r'NIFTY_MIDCAP_100.csv')
    nfty_mdcp_100 = df["NIFTY_MIDCAP_100"].tolist()
    s['nfty_mdcp_100'] = nfty_mdcp_100
    # print(nfty_mdcp_100)
    return nfty_mdcp_100

nifty_midcap_100()

def nifty_next_50():
    df = pd.read_csv(r'NIFTY_NEXT_50.csv')
    nfty_nxt_50 = df["NIFTY_NEXT_50"].tolist()
    s['nfty_nxt_50'] = nfty_nxt_50
    # print(nfty_nxt_50)
    return nfty_nxt_50

nifty_next_50()

def nifty_oil_and_gas():
    df = pd.read_csv(r'NIFTY_OIL_AND_GAS.csv')
    nfty_oil_and_gas = df["NIFTY_OIL_AND_GAS"].tolist()
    s['nfty_oil_and_gas'] = nfty_oil_and_gas
    # print(nfty_oil_and_gas)
    return nfty_oil_and_gas

nifty_oil_and_gas()

def nifty_pharma():
    df = pd.read_csv(r'NIFTY_PHARMA.csv')
    nfty_pharma = df["NIFTY_PHARMA"].tolist()
    s['nfty_pharma'] = nfty_pharma
    print(nfty_pharma)
    return nfty_pharma

nifty_pharma()

def nifty_psu_bank():
    df = pd.read_csv(r'NIFTY_PSU_BANK.csv')
    nfty_psu_bank = df["NIFTY_PSU_BANK"].tolist()
    s['nfty_psu_bank'] = nfty_psu_bank
    print("psu bank",nfty_psu_bank)
    return nfty_psu_bank

nifty_psu_bank()

def nifty_realty():
    df = pd.read_csv(r'NIFTY_REALTY.csv')
    nfty_realty = df["NIFTY_REALTY"].tolist()
    s['nfty_realty'] = nfty_realty
    print(nfty_realty)
    return nfty_realty

nifty_realty()


def nifty_equity_to_trade():
    df = pd.read_csv(r'EQUITY_TO_TRADE.csv')
    nfty_eqty_to_trd = df["EQUITY_TO_TRADE"].tolist()
    s['nfty_eqty_to_trd'] = nfty_eqty_to_trd
    # print(nfty_eqty_to_trd)
    return nfty_eqty_to_trd

nifty_equity_to_trade()

s.close()






