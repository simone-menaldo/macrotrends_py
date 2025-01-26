'''
Macrotrends - Global Metrics
'''

# Libraries
import ast
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

# Global variables
HEADER = {'User-Agent': 'Mozilla/5.0'}

# Population class
class Population:

    def __init__(self):
        pass

    # Get the total population by country
    def get_tot_pop() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/population"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)
        
                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the population growth rate by country
    def get_pop_growth() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/population-growth-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the population density by country
    def get_pop_density() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/population-density"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the urban population by country
    def get_pop_urban() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/urban-population"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the rural population by country
    def get_pop_rural() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/rural-population"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the life expectancy by country
    def get_life_exp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/life-expectancy"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)
        
                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the birth rate by country
    def get_birth_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/birth-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the death rate by country
    def get_death_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/death-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the infant mortality rate by country
    def get_infant_mort() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/infant-mortality-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the fertility rate by country
    def get_fert_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/fertility-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Economy class
class Economy:

    def __init__(self):
        pass

    # Get the GDP by country
    def get_gdp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/gdp-gross-domestic-product"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the GDP growth rate by country
    def get_gdp_growth() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/gdp-growth-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the GDP per capita by country
    def get_gdp_capita() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/gdp-per-capita"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the GNI by country
    def get_gni() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/gni-gross-national-income"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the GNI per capita by country
    def get_gni_capita() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/gni-per-capita"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the debt to GDP ratio by country
    def get_debt_to_gdp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/debt-to-gdp-ratio"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the GNP by country
    def get_gnp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/gnp-gross-national-product"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the inflation rate by country
    def get_inflation() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/inflation-rate-cpi"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the economic growth rate by country
    def get_econ_growth() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/economic-growth-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the manufacturing level by country
    def get_manufacturing() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/manufacturing-output"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Trade class
class Trade:

    def __init__(self):
        pass

    # Get the trade balance by country
    def get_trade_balance() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/trade-balance-deficit"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the trade to GDP ratio by country
    def get_trade_to_gdp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/trade-gdp-ratio"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the total exports by country
    def get_exports() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/exports"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the total imports by country
    def get_imports() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/imports"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the Foreign Direct Investment by country
    def get_fdi() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/foreign-direct-investment"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the tariff rates by country
    def get_tariffs() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/tariff-rates"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the tourism statistics by country
    def get_tourism_stats() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/tourism-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Health class
class Health:

    def __init__(self):
        pass

    # Get the healthcare spending by country
    def get_health_spend() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/healthcare-spending"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the maternal mortality rate by country
    def get_maternal_mort() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/maternal-mortality-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the smoking rate by country
    def get_smoking_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/smoking-rate-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Education class
class Education:

    def __init__(self):
        pass

    # Get the literacy rate by country
    def get_literacy_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/literacy-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Development class
class Development:

    def __init__(self):
        pass

    # Get the poverty rate by country
    def get_poverty_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/poverty-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('$', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the hunger statistics by country
    def get_hunger_stats() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/hunger-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the clean water access by country
    def get_clean_water() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/clean-water-access-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the electricity access by country
    def get_electricity() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/electricity-access-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Labor Force class
class LaborForce:

    def __init__(self):
        pass

    # Get the unemployment rate by country
    def get_unemp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/unemployment-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the youth unemployment rate by country
    def get_youth_unemp() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/youth-unemployment-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the participation rate by country
    def get_part_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/labor-force-participation-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Environment class
class Environment:

    def __init__(self):
        pass

    # Get the carbon emissions by country
    def get_co2() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/carbon-co2-emissions"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the greenhouse gas emissions by country
    def get_ghg() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/ghg-greenhouse-gas-emissions"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the renewable energy by country
    def get_renew() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/renewable-energy-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the fossil fuel by country
    def get_fossil_fuel() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/fossil-fuel-consumption"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the coal consumption by country
    def get_coal() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/coal-usage-consumption"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Crime class
class Crime:

    def __init__(self):
        pass

    # Get the crime rate by country
    def get_crime_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/crime-rate-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the murder rate by country
    def get_murder_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/murder-homicide-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Immigration class
class Immigration:

    def __init__(self):
        pass

    # Get the immigration statistics by country
    def get_immigration_stats() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/immigration-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the net migration by country 
    def get_net_migration() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/net-migration"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the refugee statistics by country
    def get_refugee_stats() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/refugee-statistics"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")
    
# Other class
class Other:

    def __init__(self):
        pass

    # Get the military spending by country
    def get_military_spending() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/military-spending-defense-budget"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the military size by country
    def get_military_size() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/military-army-size"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the suicide rate by country
    def get_suicide_rate() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/suicide-rate"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the education spending by country
    def get_edu_spending() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/education-spending"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the surface area by country
    def get_surface() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/surface-area-km"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")

    # Get the arable land by country
    def get_arable_land() -> pd.DataFrame:

        url = f"https://www.macrotrends.net/global-metrics/countries/ranking/arable-land"
        res = requests.get(url=url, headers=HEADER)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')

            table = soup.find('table')
            if table:
                headers = [header.text for header in table.find_all('th')]

                rows = []
                for row in table.find_all('tr'):
                    cells = [cell.text.strip().replace(',', '').replace('%', '') for cell in row.find_all('td')]
                    if cells:
                        rows.append(cells)

                df = pd.DataFrame(rows, columns=headers)
                df.set_index(df.columns[0], inplace=True)
                df = df.astype(float)

                return df

            else:

                print("No table found")

        else:

            print(f"Data not found. Response status: {res.status_code}")