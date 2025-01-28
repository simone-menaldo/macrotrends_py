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

# Market Indexes class
class MarketIndexes:

    def __init__(self):
        pass

    # Stock market secular cycles
    def get_stock_market_cycles() -> pd.DataFrame:

        '''
        Stock market secular cycles
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1296&url=stock-market-cycles-historical-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = [", 1)[1].split(']', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df = pd.DataFrame(raw_dict)

            df = df.astype(float)
            df.set_index(df.columns[1], inplace=True)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Dow Jones - 100 year historical
    def get_dow_hist(series: str = "hist") -> pd.DataFrame:

        '''
        Dow Jones - 100 year historical
        ---------------
        Inputs:
            series: type of series to import (one of one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession'])
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1319&url=dow-jones-100-year-historical-chart"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=DJIA"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=DJIA"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=DJIA"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=DJIA"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=DJIA"
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

    # NASDAQ - 45 year historical chart
    def get_nasdaq_hist(series: str = "hist") -> pd.DataFrame:

        '''
        NASDAQ - 45 year historical chart
        ---------------
        Inputs:
            series: type of series to import (one of one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession'])
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1320&url=nasdaq-historical-chart"

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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=NASDAQCOM"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=NASDAQCOM"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=NASDAQCOM"

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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=NASDAQCOM"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=NASDAQCOM"
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

    # S&P 500 Earnings History
    def get_sp500_eps() -> pd.DataFrame:

        '''
        S&P 500 Earnings History
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1324&url=s-p-500-earnings-history"
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

    # Dow Jones - 10 Year Daily
    def get_dow_daily() -> pd.DataFrame:

        '''
        Dow Jones - 10 Year Daily
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1358&url=dow-jones-industrial-average-last-10-years"
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

    # S&P 500 - 90 Year Historical Chart
    def get_sp500_hist(series: str = "hist") -> pd.DataFrame:

        '''
        S&P 500 - 90 Year Historical Chart
        ---------------
        Inputs:
            series: type of series to import (one of one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession'])
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2324&url=sp-500-historical-chart-data"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=SP500"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=SP500"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=SP500"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=SP500"
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

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=SP500"
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

    # Stock Market Performance by President
    def get_pres_perf() -> pd.DataFrame:

        '''
        Stock Market Performance by President
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2481&url=stock-market-performance-by-president"
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

    # S&P 500 by President
    def get_sp500_pres() -> pd.DataFrame:

        '''
        S&P 500 by President
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2481&url=stock-market-performance-by-president"
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

    # Dow Jones - 1929 Bear Market
    def get_dow_1929() -> pd.DataFrame:

        '''
        Dow Jones - 1929 Bear Market
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2484&url=dow-jones-crash-1929-bear-market"
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

    # S&P 500 - 10 Year Daily
    def get_sp500_daily() -> pd.DataFrame:

        '''
        S&P 500 - 10 Year Daily
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2488&url=sp500-10-year-daily-chart"
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

    # NASDAQ - 10 Year Daily
    def get_nasdaq_daily() -> pd.DataFrame:

        '''
        NASDAQ - 10 Year Daily
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2489&url=nasdaq-composite-index-10-year-daily-chart"
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

    # S&P 500 YTD Performance
    def get_sp500_ytd() -> pd.DataFrame:

        '''
        S&P 500 YTD Performance
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2490&url=sp-500-ytd-performance"
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

    # Dow Jones YTD Performance
    def get_dow_ytd() -> pd.DataFrame:

        '''
        Dow Jones YTD Performance
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2505&url=dow-jones-ytd-performance"
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

    # S&P 500 Historical Annual Returns
    def get_sp500_rets() -> pd.DataFrame:

        '''
        S&P 500 Historical Annual Returns
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=SP500"
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

    # NASDAQ YTD Performance
    def get_nasdaq_ytd() -> pd.DataFrame:

        '''
        NASDAQ YTD Performance
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2527&url=nasdaq-ytd-performance"
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

    # Dow Jones vs NASDAQ Since 1971
    def get_dow_vs_nasdaq() -> pd.DataFrame:

        '''
        Dow Jones vs NASDAQ Since 1971
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2528&url=dow-jones-vs-NASDAQ-chart"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            
            raw_data = str(soup).split("var originalData = ", 1)[1].split(';', 1)[0]
            raw_dict = ast.literal_eval(raw_data)

            df1 = pd.DataFrame(raw_dict['1'])
            df1.set_index("date", inplace=True)
            df1 = df1.astype(float)
            df1.columns = ["DJI"]

            df2 = pd.DataFrame(raw_dict['2'])
            df2.set_index("date", inplace=True)
            df2 = df2.astype(float)
            df2.columns = ["NSDQI"]

            df = pd.concat([df1, df2], axis=1)

            return df

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Dow to GDP Ratio
    def get_dow_to_gdp() -> pd.DataFrame:

        '''
        Dow to GDP Ratio
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2574&url=dow-to-gdp-ratio-chart"
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

    # S&P 500 PE Ratio Historical Chart
    def get_sp500_pe() -> pd.DataFrame:

        '''
        S&P 500 PE Ratio Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2577&url=sp-500-pe-ratio-price-to-earnings-chart"
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

    # Shanghai Composite (China Stock Market)
    def get_shanghai_hist() -> pd.DataFrame:

        '''
        Shanghai Composite (China Stock Market)
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2592&url=shanghai-composite-index-china-stock-market-chart-data"
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

    # Nikkei 225 Index - Historical Chart
    def get_nikkei_hist() -> pd.DataFrame:

        '''
        Nikkei 225 Index - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2593&url=nikkei-225-index-historical-chart-data"
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

    # Hang Seng Composite Index - Historical Chart
    def get_hang_seng_hist() -> pd.DataFrame:

        '''
        Hang Seng Composite Index - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2594&url=hang-seng-composite-index-historical-chart-data"
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

    # DAX 30 Index - Historical Chart
    def get_dax_hist() -> pd.DataFrame:

        '''
        DAX 30 Index - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2595&url=dax-30-index-germany-historical-chart-data"
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

    # CAC 40 Index - Historical Chart
    def get_cac_hist() -> pd.DataFrame:

        '''
        CAC 40 Index - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2596&url=cac-40-index-france-historical-chart-data"
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

    # BOVESPA Index - Historical Chart
    def get_bovespa_hist() -> pd.DataFrame:

        '''
        BOVESPA Index - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2597&url=bovespa-index-brazil-historical-chart-data"
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

    # NASDAQ to Dow Jones Ratio
    def get_nasdaq_to_dow() -> pd.DataFrame:

        '''
        NASDAQ to Dow Jones Ratio
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2600&url=nasdaq-to-dow-ratio-chart"
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

    # S&P 500 vs Durable Goods Orders
    def get_sp500_vs_durables() -> pd.DataFrame:

        '''
        S&P 500 vs Durable Goods Orders
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2601&url=sp-500-vs-durable-goods-chart"
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

    # VIX Volatility Index - Historical Chart
    def get_vix_hist() -> pd.DataFrame:

        '''
        VIX Volatility Index - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2603&url=vix-volatility-index-historical-chart"
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

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Stock Market by President (From Election Date)
    def get_stock_mkt_pres() -> pd.DataFrame:

        '''
        Stock Market by President (From Election Date)
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2613&url=stock-market-performance-by-president-from-election-date"
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

    # S&P 500 by President (From Election Date)
    def get_sp500_pres() -> pd.DataFrame:

        '''
        S&P 500 by President (From Election Date)
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2614&url=sp500-performance-by-president-from-election-date"
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

    # Trump Stock Market Performance
    def get_trump_perf() -> pd.DataFrame:

        '''
        Trump Stock Market Performance
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2616&url=president-trump-stock-market-performance"
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

    # Dow Jones By Year
    def get_dow_rets() -> pd.DataFrame:

        '''
        Dow Jones By Year
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2622&url=dow-jones-by-year-historical-annual-returns"
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

    # NASDAQ By Year - Annual Returns
    def get_nasdaq_rets() -> pd.DataFrame:

        '''
        NASDAQ By Year - Annual Returns
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2623&url=nasdaq-by-year-historical-annual-returns"
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