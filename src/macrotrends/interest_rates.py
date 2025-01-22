'''
Macrotrends - Interest Rates
'''

# Libraries
import ast
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

# Interest Rates class
class InterestRates:

    def __init__(self):
        pass

    # LIBOR Rates - Historical Chart
    def get_libor_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1433&url=historical-libor-rates-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df

    # TED Spread - Historical Chart
    def get_ted_spread() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1447&url=ted-spread-historical-chart"
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

    # Federal Funds Rate - Historical Chart
    def get_fedrate_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2015&url=fed-funds-rate-historical-chart"
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

    # 10 Year Treasury Rate - Historical Chart
    def get_10y_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2016&url=10-year-treasury-bond-rate-yield-chart"
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

    # 1 Year Treasury Rate - Historical Chart
    def get_1y_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2492&url=1-year-treasury-rate-yield-chart"
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

    # 1 Year LIBOR Rate - Historical Chart
    def get_1y_libor() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2515&url=1-year-libor-rate-historical-chart"
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

    # 1 Month LIBOR Rate - Historical Chart
    def get_1m_libor() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2518&url=1-month-libor-rate-historical-chart"
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

    # 6 Month LIBOR Rate - Historical Chart
    def get_6m_libor() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2519&url=6-month-libor-rate-historical-chart"
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

    # 3 Month LIBOR Rate - Historical Chart
    def get_3m_libor() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2520&url=3-month-libor-rate-historical-chart"
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

    # 30 Year Treasury Rate - Historical Chart
    def get_30y_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2521&url=30-year-treasury-bond-rate-yield-chart"
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

    # 5 Year Treasury Rate - Historical Chart
    def get_5y_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2522&url=5-year-treasury-bond-rate-yield-chart"
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

    # 30 Year Fixed Mortgage Rate - Historical Chart
    def get_30y_mort() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2604&url=30-year-fixed-mortgage-rate-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

        return df