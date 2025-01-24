'''
Macrotrends - Market Indexes
'''

# Libraries
import ast
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

# Precious Metals class
class PreciousMetals:

    def __init__(self):
        pass

    # Gold Prices - 100 Year Historical Chart
    def get_gold_hist(series: str = "hist") -> pd.DataFrame:

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1333&url=historical-gold-prices-100-year-chart"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.iloc[:, 1:]

                df.set_index("date", inplace=True)
                df = df.astype(float)

        elif series == "10y":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=GOLDAMGBD228NLBM"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.iloc[:, 1:]

                df.set_index("date", inplace=True)
                df = df.astype(float)

        elif series == "by_year":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=GOLDAMGBD228NLBM"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.iloc[:, 1:]

                df.set_index("date", inplace=True)
                df = df.astype(float)

        elif series == "by_president":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=GOLDAMGBD228NLBM"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

        elif series == "by_fed":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=GOLDAMGBD228NLBM"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

        elif series == "by_recession":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=GOLDAMGBD228NLBM"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

        return df
            
    # Gold Prices vs Oil Prices
    def get_gold_vs_oil() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1334&url=gold-prices-vs-oil-prices-historical-correlation"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Gold Prices and U.S Dollar Correlation
    def get_gold_usd_corr() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1335&url=dollar-vs-gold-comparison-last-ten-years"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Dow to Gold Ratio
    def get_dow_to_gold() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1378&url=dow-to-gold-ratio-100-year-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Gold to Oil Ratio
    def get_gold_to_oil() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1380&url=gold-to-oil-ratio-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # S&P 500 to Gold Ratio
    def get_sp500_to_gold() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1437&url=sp500-to-gold-ratio-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # XAU to Gold Ratio
    def get_xau_to_gold() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1439&url=xau-to-gold-ratio"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # HUI to Gold Ratio
    def get_hui_to_gold() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1440&url=hui-to-gold-ratio"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Gold to Silver Ratio
    def get_gold_to_silver() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1441&url=gold-to-silver-ratio"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Silver Prices - 100 Year Historical Chart
    def get_silver_hist(series: str = "hist") -> pd.DataFrame:

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1470&url=historical-silver-prices-100-year-chart"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.iloc[:, 1:]

                df.set_index("date", inplace=True)
                df = df.astype(float)

        elif series == "10y":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=SILVER"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.iloc[:, 1:]

                df.set_index("date", inplace=True)
                df = df.astype(float)

        elif series == "by_year":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=SILVER"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.iloc[:, 1:]

                df.set_index("date", inplace=True)
                df = df.astype(float)

        elif series == "by_president":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=SILVER"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

        elif series == "by_fed":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=SILVER"

            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

        elif series == "by_recession":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=SILVER"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

        return df

    # Fed Balance Sheet vs Gold Price
    def get_fed_vs_gold() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1486&url=fed-balance-sheet-vs-gold-price"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = ", 1)[1].split(';', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df1 = pd.DataFrame(raw_dict['1'])
            df1.set_index("date", inplace=True)
            df1 = df1.astype(float)
            df1.columns = ["FED_BS"]

            df2 = pd.DataFrame(raw_dict['2'])
            df2.set_index("date", inplace=True)
            df2 = df2.astype(float)
            df2.columns = ["GOLD"]

            df = pd.concat([df1, df2], axis=1)

        return df

    # Gold to Monetary Base Ratio
    def get_gold_to_mb() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2485&url=gold-to-monetary-base-ratio"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Gold Prices vs Silver Prices
    def get_gold_vs_silver() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2517&url=gold-prices-vs-silver-prices-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Platinum Prices - Historical Chart
    def get_platinum_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2540&url=platinum-prices-historical-chart-data"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.drop("id", axis=1, inplace=True)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Platinum Prices vs Gold Prices
    def get_platinum_vs_gold() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2541&url=platinum-prices-vs-gold-prices"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Palladium Prices - Historical Chart
    def get_palladium_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2542&url=palladium-prices-historical-chart-data"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df.drop("id", axis=1, inplace=True)
            df = df.astype(float)

        return df

    # Gold Price vs Stock Market
    def get_gold_vs_mkt() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2608&url=gold-price-vs-stock-market-100-year-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = ", 1)[1].split(';', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df1 = pd.DataFrame(raw_dict['1'])
            df1.set_index("date", inplace=True)
            df1 = df1.astype(float)
            df1.columns = ["GOLD"]

            df2 = pd.DataFrame(raw_dict['2'])
            df2.set_index("date", inplace=True)
            df2 = df2.astype(float)
            df2.columns = ["MKT"]

            df = pd.concat([df1, df2], axis=1)

        return df

    # Dow to Silver Ratio
    def get_dow_to_silver() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2610&url=dow-to-silver-ratio-100-year-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Silver to Oil Ratio
    def get_silver_to_oil() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2612&url=silver-to-oil-ratio-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # Gold Price - Last 10 Years
    def get_gold_price() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2627&url=gold-price-last-ten-years"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df = df.iloc[:, 1:]

            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # S&P 500 vs Fed Funds Rate
    def get_sp500_fedrate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2638&url=sp500-fed-funds-rate-compared"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df