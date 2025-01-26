'''
Macrotrends - Commodities
'''

# Libraries
import ast
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

# Commodities class
class Commodities:

    def __init__(self):
        pass

    # Copper Prices - Historical Chart
    def get_copper_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1476&url=copper-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Soybean Prices - Historical Chart
    def get_soybean_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2531&url=soybean-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Corn Prices - Historical Chart
    def get_corn_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2532&url=corn-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Cotton Prices - Historical Chart
    def get_cotton_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2533&url=cotton-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Wheat Prices - Historical Chart
    def get_wheat_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2534&url=wheat-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Coffee Prices - Historical Chart
    def get_coffee_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2535&url=coffee-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Oats Prices - Historical Chart
    def get_oats_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2536&url=oats-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Sugar Prices - Historical Chart
    def get_sugar_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2537&url=sugar-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Soybean Oil Prices - Historical Chart
    def get_soybean_oil_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2538&url=soybean-oil-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Lumber Prices - Historical Chart
    def get_lumber_hist() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2637&url=lumber-prices-historical-chart-data"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")