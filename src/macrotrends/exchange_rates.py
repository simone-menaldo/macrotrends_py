'''
Macrotrends - Exchange Rates
'''

# Libraries
import ast
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

# Exchange Rates class
class ExchangeRates:

    def __init__(self):
        pass

    # Dollar Index Historical Chart
    def get_usd_idx_hist() -> pd.DataFrame:

        '''
        Dollar Index Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1329&url=us-dollar-index-historical-chart"
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

    # Euro Dollar Exchange Rate - Historical Chart
    def get_eur_usd_hist() -> pd.DataFrame:

        '''
        Euro Dollar Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2548&url=euro-dollar-exchange-rate-historical-chart"
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

    # Pound Dollar Exchange Rate - Historical Chart
    def get_gbp_usd_hist() -> pd.DataFrame:

        '''
        Pound Dollar Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2549&url=pound-dollar-exchange-rate-historical-chart"
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

    # Dollar Yen Exchange Rate - Historical Chart
    def get_usd_jpy_hist() -> pd.DataFrame:

        '''
        Dollar Yen Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2550&url=dollar-yen-exchange-rate-historical-chart"
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

    # AUD US Dollar Exchange Rate - Historical Chart
    def get_aud_usd_hist() -> pd.DataFrame:

        '''
        AUD US Dollar Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2551&url=australian-us-dollar-exchange-rate-historical-chart"
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

    # Euro Swiss Franc Exchange Rate - Historical Chart
    def get_eur_chf_hist() -> pd.DataFrame:

        '''
        Euro Swiss Franc Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2552&url=euro-swiss-franc-exchange-rate-historical-chart"
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

    # Euro Pound Exchange Rate - Historical Chart
    def get_eur_gbp_hist() -> pd.DataFrame:

        '''
        Euro Pound Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2553&url=euro-british-pound-exchange-rate-historical-chart"
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

    # Euro Yen Exchange Rate - Historical Chart
    def get_eur_jpy_hist() -> pd.DataFrame:

        '''
        Euro Yen Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2553&url=euro-british-pound-exchange-rate-historical-chart"
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

    # Pound Yen Exchange Rate - Historical Chart
    def get_gbp_jpy_hist() -> pd.DataFrame:

        '''
        Pound Yen Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2556&url=pound-japanese-yen-exchange-rate-historical-chart"
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

    # NZD - US Dollar Exchange Rate - Historical Chart
    def get_nzd_usd_hist() -> pd.DataFrame:

        '''
        NZD - US Dollar Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2557&url=new-zealand-us-dollar-exchange-rate-historical-chart"
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

    # US Dollar Franc Exchange Rate - Historical Chart
    def get_usd_chf_hist() -> pd.DataFrame:

        '''
        US Dollar Franc Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2558&url=us-dollar-swiss-franc-exchange-rate-historical-chart"
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

    # US Dollar Peso Exchange Rate - Historical Chart
    def get_usd_mxn_hist() -> pd.DataFrame:

        '''
        US Dollar Peso Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2559&url=us-dollar-mexican-peso-exchange-rate-historical-chart"
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

    # USD SGD Exchange Rate - Historical Chart
    def get_usd_sdg_hist() -> pd.DataFrame:

        '''
        USD SGD Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2561&url=us-dollar-singapore-exchange-rate-historical-chart"
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

    # Dollar Yuan Exchange Rate - Historical Chart
    def get_usd_cny_hist() -> pd.DataFrame:

        '''
        Dollar Yuan Exchange Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2575&url=us-dollar-yuan-exchange-rate-historical-chart"
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