'''
Macrotrends - Stock Research
'''

# Libraries
import ast
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

IS_FIELDS = [
    "revenue", "cost-goods-sold", "gross-profit", "research-development-expenses", \
    "selling-general-administrative-expenses", "operating-expenses", "operating-income", \
    "total-non-operating-income-expense", "pre-tax-income", "total-provision-income-taxes", \
    "income-after-taxes", "income-from-continuous-operations", "net-income", "ebitda", \
    "ebit", "basic-shares-outstanding", "shares-outstanding", "eps-basic-net-earnings-per-share", \
    "eps-earnings-per-share-diluted"
]

BS_FIELDS = [
    "cash-on-hand", "receivables", "inventory", "other-current-assets", "total-current-assets", \
    "net-property-plant-equipment", "long-term-investments", "goodwill-intangible-assets-total", \
    "other-long-term-assets", "total-long-term-assets", "total-assets", "total-current-liabilities", \
    "long-term-debt", "other-non-current-liabilities", "total-long-term-liabilities", "total-liabilities", \
    "common-stock-net", "retained-earnings-accumulated-deficit", "comprehensive-income", \
    "total-share-holder-equity", "total-liabilities-share-holders-equity"
]

CF_FIELDS = [
    "net-income-loss", "total-depreciation-amortization-cash-flow", "other-non-cash-items", \
    "total-non-cash-items", "change-in-accounts-receivable", "change-in-inventories", \
    "change-in-accounts-payable", "change-in-assets-liabilities", "cash-flow-from-operating-activities", \
    "net-change-in-property-plant-equipment", "net-change-in-intangible-assets", "net-acquisitions-divestitures", \
    "net-change-in-short-term-investments", "net-change-in-long-term-investments", \
    "net-change-in-investments-total", "investing-activities-other", "cash-flow-from-investing-activities", \
    "net-long-term-debt", "net-current-debt", "debt-issuance-retirement-net-total", \
    "net-common-equity-issued-repurchased", "net-total-equity-issued-repurchased", \
    "total-common-preferred-stock-dividends-paid", "financial-activities-other", \
    "cash-flow-from-financial-activities", "net-cash-flow", "stock-based-compensation", \
    "common-stock-dividends-paid"
]

FR_FIELDS = [
    "current-ratio", "long-term-debt-capital", "debt-equity-ratio", "gross-margin", "operating-margin", \
    "ebit-margin", "ebitda-margin", "pre-tax-profit-margin", "net-profit-margin", "asset-turnover", \
    "inventory-turnover", "receiveable-turnover", "days-sales-in-receivables", "roe", \
    "return-on-tangible-equity", "roa", "roi", "book-value-per-share", "operating-cash-flow-per-share", \
    "free-cash-flow-per-share"
]

# Prices class
class Prices:

    def __init__(self):
        pass

    # Get the historical prices for a single stock
    def get_prices_hist(symbol: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/stock_price_history.php?t={symbol}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var dataDaily = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
            df['d'] = pd.to_datetime(df['d'])
            df.set_index('d', inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the raw historical prices without stock split adjustments for a single stock
    def get_stock_splits(symbol: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/stock_splits.php?t={symbol}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var dataDaily = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical market capitalization for a single stock
    def get_market_cap(symbol: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/market_cap.php?t={symbol}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.iloc[:, 1:] = df.iloc[:, 1:].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Financials class
class Financials:

    def __init__(self):
        pass

    # Get the historical income statement figures for a single stock
    def get_is(symbol: str, field: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/popup_fundamental.php?t={symbol}&s={field}&freq={freq}&statement=financial-statements"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical balance sheet figures for a single stock
    def get_bs(symbol: str, field: str, freq) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/popup_fundamental.php?t={symbol}&s={field}&freq={freq}&statement=balance-sheet"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical cash flow statement figures for a single stock
    def get_cf(symbol: str, field: str, freq) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/popup_fundamental.php?t={symbol}&s={field}&freq={freq}&statement=cash-flow-statement"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical financial ratios for a single stock
    def get_fr(symbol: str, field: str, freq) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/popup_fundamental.php?t={symbol}&s={field}&freq={freq}&statement=financial-ratios"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Revenue & Profit class
class RevenueProfit:

    def __init__(self):
        pass

    # Get the historical revenues for a single stock
    def get_revenue(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=revenue&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical gross profit for a single stock
    def get_gross_profit(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=gross-profit&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical operating income for a single stock
    def get_op_income(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=operating-income&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical EBITDA for a single stock
    def get_ebitda(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=ebitda&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical net income for a single stock
    def get_net_income(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=net-income&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical EPS for a single stock
    def get_eps(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=eps-earnings-per-share-diluted&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
    # Get the historical shares outstanding for a single stock
    def get_shares_out(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=shares-outstanding&statement=income-statement&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Assets & Liabilities class
class AssetsLiabilities:

    def __init__(self):
        pass

    # Get the historical total assets for a single stock
    def get_tot_assets(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=total-assets&statement=balance-sheet&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical cash on hands for a single stock
    def get_cash(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=cash-on-hand&statement=balance-sheet&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical long term debt for a single stock
    def get_lt_debt(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=long-term-debt&statement=balance-sheet&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical total liabilities for a single stock
    def get_tot_liab(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=total-liabilities&statement=balance-sheet&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical shareholders equity for a single stock
    def get_sh_equity(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=total-share-holder-equity&statement=balance-sheet&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Margins class
class Margins:

    def __init__(self):
        pass

    # Get the historical profit margin for a single stock
    def get_profit_margin(symbol: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_metric.php?t={symbol}&chart=profit-margin"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical gross margin for a single stock
    def get_gross_margin(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=gross-margin&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical operating margin for a single stock
    def get_op_margin(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=operating-margin&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical EBITDA margin for a single stock
    def get_ebitda_margin(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=ebitda-margin&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical pre-tax margin for a single stock
    def get_pretax_margin(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=pre-tax-profit-margin&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical net margin for a single stock
    def get_net_margin(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=net-profit-margin&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Price Ratios class
class PriceRatios:

    def __init__(self):
        pass

    # Get the historical PE ratio for a single stock
    def get_pe(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=pe-ratio&statement=price-ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical P/S ratio for a single stock
    def get_ps(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=price-sales&statement=price-ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical P/B ratio for a single stock
    def get_pb(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=price-book&statement=price-ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical price-FCF ratio ratio for a single stock
    def get_pfcf(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=price-fcf&statement=price-ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical net worth for a single stock
    def get_net_worth(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/market_cap.php?t={symbol}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Other Ratios class
class OtherRatios:

    def __init__(self):
        pass

    # Get the historical current ratio for a single stock
    def get_cr(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=current-ratio&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical quick ratio for a single stock
    def get_qr(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=quick-ratio&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical D/E ratio for a single stock
    def get_de(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=debt-equity-ratio&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical ROE for a single stock
    def get_roe(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=roe&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical ROA for a single stock
    def get_roa(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=roa&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical ROI for a single stock
    def get_roi(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=roi&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical Return Tang Equity for a single stock
    def get_rte(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=return-on-tangible-equity&statement=ratios&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")
        
# Other Metrics class
class OtherMetrics:

    def __init__(self):
        pass

    # Get the historical dividend yield for a single stock
    def get_div_yield(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/dividend_yield.php?t={symbol}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the historical number of employees for a single stock
    def get_num_employees(symbol: str, freq: str) -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/fundamental_iframe.php?t={symbol}&type=number-of-employees&statement=&freq={freq}"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var chartData = [", 1)[1].split(']', 1)[0]
            raw_data = raw_data.replace("null", '"NULL"')
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df.replace("NULL", np.nan, inplace=True)
            df[df.columns[1:]] = df[df.columns[1:]].astype(float)
            df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
            df.set_index(df.columns[0], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")