'''
Macrotrends - Economy
'''

# Libraries
import ast
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

# Energy class
class Energy:

    def __init__(self):
        pass

    # Crude Oil Prices - 70 Year Historical Chart
    def get_cl_hist(series: str = "hist") -> pd.DataFrame:

        '''
        Crude Oil Prices - 70 Year Historical Chart
        ---------------
        Inputs:
            series: type of series to import (one of one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession'])
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1369&url=crude-oil-price-history-chart"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "10y":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=DCOILWTICO"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_year":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=DCOILWTICO"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_president":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=DCOILWTICO"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_fed":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=DCOILWTICO"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_recession":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=DCOILWTICO"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

    # Crude Oil vs S&P 500
    def get_cl_vs_sp500() -> pd.DataFrame:

        '''
        Crude Oil vs S&P 500
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1453&url=crude-oil-vs-the-s-p-500"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Natural Gas Prices - Historical Chart
    def get_ng_hist(series: str = "hist") -> pd.DataFrame:

        '''
        Natural Gas Prices - Historical Chart
        ---------------
        Inputs:
            series: type of series to import (one of one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession'])
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2478&url=natural-gas-prices-historical-chart"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "10y":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=DHHNGSP"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_year":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=DHHNGSP"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_president":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=DHHNGSP"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_fed":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=DHHNGSP"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_recession":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=DHHNGSP"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Heating Oil - Historical Chart
    def get_ho_hist(series: str = "hist") -> pd.DataFrame:

        '''
        Heating Oil - Historical Chart
        ---------------
        Inputs:
            series: type of series to import (one of one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession'])
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2479&url=heating-oil-prices-historical-chart-data"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "10y":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=DHOILNYH"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_year":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=DHOILNYH"
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

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_president":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=DHOILNYH"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_fed":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=DHOILNYH"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)

                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

        elif series == "by_recession":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=DHOILNYH"
            res = requests.get(url=url, headers=HEADER)

            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                
                raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
                raw_dict = ast.literal_eval(raw_data)

                df = pd.DataFrame(raw_dict)
                df = df.astype(float)
            
                return df

            else:

                print(f"Data not found. Response status: {res.status_code}")

    # Brent Crude Oil Prices - 10 Year Daily
    def get_brent_daily() -> pd.DataFrame:

        '''
        Brent Crude Oil Prices - 10 Year Daily
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2480&url=brent-crude-oil-prices-10-year-daily-chart"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Oil Prices vs Natural Gas
    def get_oil_vs_ng() -> pd.DataFrame:

        '''
        Oil Prices vs Natural Gas
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2500&url=crude-oil-vs-natural-gas-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Oil Prices vs Gasoline Prices
    def get_oil_vs_gasoline() -> pd.DataFrame:

        '''
        Oil Prices vs Gasoline Prices
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2501&url=crude-oil-vs-gasoline-prices-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Oil Prices vs Propane Prices
    def get_oil_vs_propane() -> pd.DataFrame:

        '''
        Oil Prices vs Propane Prices
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2502&url=crude-oil-vs-propane-prices-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # WTI Crude Oil - 10 Year Daily
    def get_wti_daily() -> pd.DataFrame:

        '''
        WTI Crude Oil - 10 Year Daily
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&url=wti-crude-oil-prices-10-year-daily-chart"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # U.S. Crude Oil Production
    def get_us_oil_prod() -> pd.DataFrame:

        '''
        U.S. Crude Oil Production
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2562&url=us-crude-oil-production-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # U.S. Crude Oil Exports
    def get_us_oil_exp() -> pd.DataFrame:

        '''
        U.S. Crude Oil Exports
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2563&url=us-crude-oil-exports-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Saudi Arabia Crude Oil Production
    def get_saudi_oil_prod() -> pd.DataFrame:

        '''
        Saudi Arabia Crude Oil Production
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2564&url=saudi-arabia-crude-oil-production-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # U.S. Crude Oil Reserves
    def get_us_oil_reserves() -> pd.DataFrame:

        '''
        U.S. Crude Oil Reserves
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2565&url=us-crude-oil-reserves-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)
            df.set_index("date", inplace=True)
            df = df.astype(float)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")