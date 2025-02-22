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

# Economy class
class Economy:

    def __init__(self):
        pass

    # Housing Starts
    def get_housing_starts() -> pd.DataFrame:

        '''
        Housing Starts
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1314&url=housing-starts-historical-chart"
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

    # National Unemployment Rate
    def get_unemp() -> pd.DataFrame:

        '''
        National Unemployment Rate
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1316&url=us-national-unemployment-rate"
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

    # Initial Jobless Claims - Historical Chart
    def get_init_jobless_claims() -> pd.DataFrame:

        '''
        Initial Jobless Claims - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1365&url=jobless-claims-historical-chart"
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

    # Real Retail Sales
    def get_retail_sales() -> pd.DataFrame:

        '''
        Real Retail Sales
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1371&url=retail-sales-historical-chart"
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

    # Auto and Light Truck Sales Historical Chart
    def get_auto_sales() -> pd.DataFrame:

        '''
        Auto and Light Truck Sales Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1372&url=auto-and-light-truck-sales-historical-chart"
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

    # U6 Unemployment Rate
    def get_u6_unemp() -> pd.DataFrame:

        '''
        U6 Unemployment Rate
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1377&url=u6-unemployment-rate"
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

    # Debt to GDP Ratio
    def get_debt_to_gdp() -> pd.DataFrame:

        '''
        Debt to GDP Ratio
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=1381&url=debt-to-gdp-ratio-historical-chart"
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

    # National Debt By President
    def get_debt_pres() -> pd.DataFrame:

        '''
        National Debt By President
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''
        pass

    # National Debt by Year
    def get_debt_by_year() -> pd.DataFrame:

        '''
        National Debt by Year
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2496&url=national-debt-growth-by-year"
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

    # Historical Inflation Rate by Year
    def get_infl_by_year() -> pd.DataFrame:

        '''
        Historical Inflation Rate by Year
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2497&url=historical-inflation-rate-by-year"
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

    # Unemployment Rate by Race
    def get_unemp_race() -> pd.DataFrame:

        '''
        Unemployment Rate by Race
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2508&url=unemployment-rate-by-race"
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

    # Unemployment Rate by Education
    def get_unemp_edu() -> pd.DataFrame:

        '''
        Unemployment Rate by Education
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2509&url=unemployment-rate-by-education"
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

    # Unemployment Rate - College Graduates
    def get_unemp_grad() -> pd.DataFrame:

        '''
        Unemployment Rate - College Graduates
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2510&url=unemployment-rate-college-graduates"
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

    # Unemployment Rate - Men vs Women
    def get_unemp_sex() -> pd.DataFrame:

        '''
        Unemployment Rate - Men vs Women
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2511&url=unemployment-rate-men-women"
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

    # Durable Goods Orders - Historical Chart
    def get_goods_orders(series: str = "hist") -> pd.DataFrame:

        '''
        Durable Goods Orders - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        if series not in ["hist", "10y", "by_year", "by_president", "by_fed", "by_recession"]:
            raise ValueError("Series parameter must be one of ['hist', '10y', 'by_year', 'by_president', 'by_fed', 'by_recession']")

        if series == "hist":

            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2582&url=durable-goods-orders-historical-chart"
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
        
            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2516&template=3&series_id=DGORDER"
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
        
            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=50&series_id=DGORDER"
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
        
            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=6&series_id=DGORDER"
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
        
            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=9&series_id=DGORDER"
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
        
            url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?template=7&series_id=DGORDER"
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

    # Industrial Production - Historical Chart
    def get_ind_prod() -> pd.DataFrame:

        '''
        Industrial Production - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2583&url=industrial-production-historical-chart"
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

    # 5 Year 5 Year Forward Inflation Expectation
    def get_5y_fwd_infl() -> pd.DataFrame:

        '''
        5 Year 5 Year Forward Inflation Expectation
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2584&url=5-year-5-year-forward-inflation-rate-chart"
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

    # Capacity Utilization Rate - Historical Chart
    def get_capacity_util() -> pd.DataFrame:

        '''
        Capacity Utilization Rate - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2585&url=capacity-utilization-rate-historical-chart"
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

    # Black Unemployment Rate
    def get_black_unemp() -> pd.DataFrame:

        '''
        Black Unemployment Rate
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2621&url=black-unemployment-rate"
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

    # Continued Jobless Claims - Historical Chart
    def get_cont_jobless_claims() -> pd.DataFrame:

        '''
        Continued Jobless Claims - Historical Chart
        ---------------
        Inputs:
            None
        Output:
            df: Pandas dataframe with the values of the required metric
        '''

        url = f"https://www.macrotrends.net/assets/php/chart_iframe_comp.php?id=2629&url=continued-jobless-claims-historical-chart"
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