# Macrotrends Python API
Python library for requesting Macrotrends data

## Stock Research

1. Prices:
    1. `get_prices_hist`: get the historical prices for a single stock
    2. `get_stock_splits`: get the raw historical prices without stock split adjustments for a single stock
    3. `get_market_cap`: get the historical market capitalization for a single stock
2. Financials:
    1. `get_is`: get the historical income statement figures for a single stock
    2. `get_bs`: get the historical balance sheet figures for a single stock
    3. `get_cf`: get the historical cash flow statement figures for a single stock
    4. `get_fr`: get the historical financial ratios for a single stock
3. Revenue & Profit:
    1. `get_revenue`: get the historical revenues for a single stock
    2. `get_gross_profit`: get the historical gross profit for a single stock
    3. `get_op_income`: get the historical operating income for a single stock
    4. `get_ebitda`: get the historical EBITDA for a single stock
    5. `get_net_income`: get the historical net income for a single stock
    6. `get_eps`: get the historical EPS for a single stock
    7. `get_shares_out`: get the historical shares outstanding for a single stock
4. Assets & Liabilities:
    1. `get_tot_assets`: get the historical total assets for a single stock
    2. `get_cash`: get the historical cash on hands for a single stock
    3. `get_lt_debt`: get the historical long term debt for a single stock
    4. `get_tot_liab`: get the historical total liabilities for a single stock
    5. `get_sh_equity`: get the historical shareholders equity for a single stock
5. Margins:
    1. `get_profit_margin`: get the historical profit margin for a single stock
    2. `get_gross_margin`: get the historical gross margin for a single stock
    3. `get_op_margin`: get the historical operating margin for a single stock
    4. `get_ebitda_margin`: get the historical EBITDA margin for a single stock
    5. `get_pretax_margin`: get the historical pre-tax margin for a single stock
    6. `get_net_margin`: get the historical net margin for a single stock
6. Price Ratios:
    1. `get_pe`: get the historical PE ratio for a single stock
    2. `get_ps`: get the historical P/S ratio for a single stock
    3. `get_pb`: get the historical P/B ratio for a single stock
    4. `get_pfcf`: get the historical price-FCF ratio ratio for a single stock
    5. `get_net_worth`: get the historical net worth for a single stock
7. Other Ratios:
    1. `get_cr`: get the historical current ratio for a single stock
    2. `get_qr`: get the historical quick ratio for a single stock
    3. `get_de`: get the historical D/E ratio for a single stock
    4. `get_roe`: get the historical ROE for a single stock
    5. `get_roa`: get the historical ROA for a single stock
    6. `get_roi`: get the historical ROI for a single stock
    7. `get_rte`: get the historical Return Tang Equity for a single stock
8. Other Metrics:
    1. `get_div_yield`: get the historical dividend yield for a single stock
    2. `get_num_employees`: get the historical number of employees for a single stock

## Market Indexes

1. `get_stock_market_cycles`: stock market secular cycles
2. `get_dow_hist`: Dow Jones - 100 year historical
3. `get_nasdaq_hist`: NASDAQ - 45 year historical chart
4. `get_sp500_eps`: S&P 500 Earnings History
5. `get_dow_daily`: Dow Jones - 10 Year Daily
6. `get_sp500_hist`: S&P 500 - 90 Year Historical Chart
7. `get_pres_perf`: Stock Market Performance by President
8. `get_sp500_pres`: S&P 500 by President
9. `get_dow_1929`: Dow Jones - 1929 Bear Market
10. `get_sp500_daily`: S&P 500 - 10 Year Daily
11. `get_nasdaq_daily`: NASDAQ - 10 Year Daily
12. `get_sp500_ytd`: S&P 500 YTD Performance
13. `get_dow_ytd`: Dow Jones YTD Performance
14. `get_sp500_rets`: S&P 500 Historical Annual Returns
15. `get_nasdaq_ytd`: NASDAQ YTD Performance
16. `get_dow_vs_nasdaq`: Dow Jones vs NASDAQ Since 1971
17. `get_dow_to_gdp`: Dow to GDP Ratio
18. `get_sp500_pe`: S&P 500 PE Ratio Historical Chart
19. `get_shanghai_hist`: Shanghai Composite (China Stock Market)
20. `get_nikkei_hist`: Nikkei 225 Index - Historical Chart
21. `get_hang_seng_hist`: Hang Seng Composite Index - Historical Chart
22. `get_dax_hist`: DAX 30 Index - Historical Chart
23. `get_cac_hist`: CAC 40 Index - Historical Chart
24. `get_bovespa_hist`: BOVESPA Index - Historical Chart
25. `get_nasdaq_to_dow`: NASDAQ to Dow Jones Ratio
26. `get_sp500_vs_durables`: S&P 500 vs Durable Goods Orders
27. `get_vix_hist`: VIX Volatility Index - Historical Chart
28. `get_stock_mkt_pres`: Stock Market by President (From Election Date)
29. `get_sp500_pres`: S&P 500 by President (From Election Date)
30. `get_trump_perf`: Trump Stock Market Performance
31. `get_dow_rets`: Dow Jones By Year
32. `get_nasdaq_rets`: NASDAQ By Year - Annual Returns

## Precious Metals

1. `get_gold_hist`: Gold Prices - 100 Year Historical Chart
2. `get_gold_vs_oil`: Gold Prices vs Oil Prices
3. `get_gold_usd_corr`: Gold Prices and U.S Dollar Correlation
4. `get_dow_to_gold`: Dow to Gold Ratio
5. `get_gold_to_oil`: Gold to Oil Ratio
6. `get_sp500_to_gold`: S&P 500 to Gold Ratio
7. `get_xau_to_gold`: XAU to Gold Ratio
8. `get_hui_to_gold`: HUI to Gold Ratio
9. `get_gold_to_silver`: Gold to Silver Ratio
10. `get_silver_hist`: Silver Prices - 100 Year Historical Chart
11. `get_fed_vs_gold`: Fed Balance Sheet vs Gold Price
12. `get_gold_to_mb`: Gold to Monetary Base Ratio
13. `get_gold_vs_silver`: Gold Prices vs Silver Prices
14. `get_platinum_hist`: Platinum Prices - Historical Chart
15. `get_platinum_vs_gold`: Platinum Prices vs Gold Prices
16. `get_palladium_hist`: Palladium Prices - Historical Chart
17. `get_gold_vs_mkt`: Gold Price vs Stock Market
18. `get_dow_to_silver`: Dow to Silver Ratio
19. `get_silver_to_oil`: Silver to Oil Ratio
20. `get_gold_price`: Gold Price - Last 10 Years
21. `get_sp500_fedrate`: S&P 500 vs Fed Funds Rate

## Energy

1. `get_cl_hist`: Crude Oil Prices - 70 Year Historical Chart
2. `get_cl_vs_sp500`: Crude Oil vs S&P 500
3. `get_ng_hist`: Natural Gas Prices - Historical Chart
4. `get_ho_hist`: Heating Oil - Historical Chart
5. `get_brent_daily`: Brent Crude Oil Prices - 10 Year Daily
6. `get_oil_vs_ng`: Oil Prices vs Natural Gas
7. `get_oil_vs_gasoline`: Oil Prices vs Gasoline Prices
8. `get_oil_vs_propane`: Oil Prices vs Propane Prices
9. `get_wti_daily`: WTI Crude Oil - 10 Year Daily
10. `get_us_oil_prod`: U.S. Crude Oil Production
11. `get_us_oil_exp`: U.S. Crude Oil Exports
12. `get_saudi_oil_prod`: Saudi Arabia Crude Oil Production
13. `get_us_oil_reserves`: U.S. Crude Oil Reserves

## Commodities

1. `get_copper_hist`: Copper Prices - Historical Chart
2. `get_soybean_hist`: Soybean Prices - Historical Chart
3. `get_corn_hist`: Corn Prices - Historical Chart
4. `get_cotton_hist`: Cotton Prices - Historical Chart
5. `get_wheat_hist`: Wheat Prices - Historical Chart
6. `get_coffee_hist`: Coffee Prices - Historical Chart
7. `get_oats_hist`: Oats Prices - Historical Chart
8. `get_sugar_hist`: Sugar Prices - Historical Chart
9. `get_soybean_oil_hist`: Soybean Oil Prices - Historical Chart
10. `get_lumber_hist`: Lumber Prices - Historical Chart

## Exchange Rates

1. `get_usd_idx_hist`: Dollar Index Historical Chart
2. `get_eur_usd_hist`: Euro Dollar Exchange Rate - Historical Chart
3. `get_gbp_usd_hist`: Pound Dollar Exchange Rate - Historical Chart
4. `get_usd_jpy_hist`: Dollar Yen Exchange Rate - Historical Chart
5. `get_aud_usd_hist`: AUD US Dollar Exchange Rate - Historical Chart
6. `get_eur_chf_hist`: Euro Swiss Franc Exchange Rate - Historical Chart
7. `get_eur_gbp_hist`: Euro Pound Exchange Rate - Historical Chart
8. `get_eur_jpy_hist`: Euro Yen Exchange Rate - Historical Chart
9. `get_gbp_jpy_hist`: Pound Yen Exchange Rate - Historical Chart
10. `get_nzd_usd_hist`: NZD - US Dollar Exchange Rate - Historical Chart
11. `get_usd_chf_hist`: US Dollar Franc Exchange Rate - Historical Chart
12. `get_usd_mxn_hist`: US Dollar Peso Exchange Rate - Historical Chart
13. `get_usd_sdg_hist`: USD SGD Exchange Rate - Historical Chart
14. `get_usd_cny_hist`: Dollar Yuan Exchange Rate - Historical Chart

## Economy

1. `get_housing_starts`: Housing Starts
2. `get_unemp`: National Unemployment Rate
3. `get_init_jobless_claims`: Initial Jobless Claims - Historical Chart
4. `get_retail_sales`: Real Retail Sales
5. `get_auto_sales`: Auto and Light Truck Sales Historical Chart
6. `get_u6_unemp`: U6 Unemployment Rate
7. `get_debt_to_gdp`: Debt to GDP Ratio
8. `get_debt_pres`: National Debt By President
9. `get_debt_by_year`: National Debt by Year
10. `get_infl_by_year`: Historical Inflation Rate by Year
11. `get_unemp_race`: Unemployment Rate by Race
12. `get_unemp_edu`: Unemployment Rate by Education
13. `get_unemp_grad`: Unemployment Rate - College Graduates
14. `get_unemp_sex`: Unemployment Rate - Men vs Women
15. `get_goods_orders`: Durable Goods Orders - Historical Chart
16. `get_ind_prod`: Industrial Production - Historical Chart
17. `get_5y_fwd_infl`: 5 Year 5 Year Forward Inflation Expectation
18. `get_capacity_util`: Capacity Utilization Rate - Historical Chart
19. `get_black_unemp`: Black Unemployment Rate
20. `get_cont_jobless_claims`: Continued Jobless Claims - Historical Chart

## Interest Rates

1. `get_libor_hist`: LIBOR Rates - Historical Chart
2. `get_ted_spread`: TED Spread - Historical Chart
3. `get_fedrate_hist`: Federal Funds Rate - Historical Chart
4. `get_10y_hist`: 10 Year Treasury Rate - Historical Chart
5. `get_1y_hist`: 1 Year Treasury Rate - Historical Chart
6. `get_1y_libor`: 1 Year LIBOR Rate - Historical Chart
7. `get_1m_libor`: 1 Month LIBOR Rate - Historical Chart
8. `get_6m_libor`: 6 Month LIBOR Rate - Historical Chart
9. `get_3m_libor`: 3 Month LIBOR Rate - Historical Chart
10. `get_30y_hist`: 30 Year Treasury Rate - Historical Chart
11. `get_5y_hist`: 5 Year Treasury Rate - Historical Chart
12. `get_30y_mort`: 30 Year Fixed Mortgage Rate - Historical Chart

## Global Metrics

1. Population:
    1. `get_tot_pop`: get the total population by country
    2. `get_pop_growth`: get the population growth rate by country
    3. `get_pop_density`: get the population density by country
    4. `get_pop_urban`: get the urban population by country
    5. `get_pop_rural`: get the rural population by country
    6. `get_life_exp`: get the life expectancy by country
    7. `get_birth_rate`: get the birth rate by country
    8. `get_death_rate`: get the death rate by country
    9. `get_infant_mort`: get the infant mortality rate by country
    10. `get_fert_rate`: get the fertility rate by country
2. Economy:
    1. `get_gdp`: get the GDP by country
    2. `get_gdp_growth`: get the GDP growth rate by country
    3. `get_gdp_capita`: get the GDP per capita by country
    4. `get_gni`: get the GNI by country
    5. `get_gni_capita`: get the GNI per capita by country
    6. `get_debt_to_gdp`: get the debt to GDP ratio by country
    7. `get_gnp`: get the GNP by country
    8. `get_inflation`: get the inflation rate by country
    9. `get_econ_growth`: get the economic growth rate by country
    10. `get_manufacturing`: get the manufacturing level by country
3. Trade
    1. `get_trade_balance`: get the trade balance by country
    2. `get_trade_to_gdp`: get the trade to GDP ratio by country
    3. `get_exports`: get the total exports by country
    4. `get_imports`: get the total imports by country
    5. `get_fdi`: get the Foreign Direct Investment by country
    6. `get_tariffs`: get the tariff rates by country
    7. `get_tourism_stats`: get the tourism statistics by country
4. Health
    1. `get_health_spend`: get the healthcare spending by country
    2. `get_maternal_mort`: get the maternal mortality rate by country
    3. `get_smoking_rate`: get the smoking rate by country
5. Education:
    1. `get_literacy_rate`: get the literacy rate by country
6. Development:
    1. `get_poverty_rate`: get the poverty rate by country
    2. `get_hunger_stats`: get the hunger statistics by country
    3. `get_clean_water`: get the clean water access by country
    4. `get_electricity`: get the electricity access by country
7. Labor Force:
    1. `get_unemp`: get the unemployment rate by country
    2. `get_youth_unemp`: get the youth unemployment rate by country
    3. `get_part_rate`: get the participation rate by country
8. Environment:
    1. `get_co2`: get the carbon emissions by country
    2. `get_ghg`: get the greenhouse gas emissions by country
    3. `get_renew`: get the renewable energy by country
    4. `get_fossil_fuel`: get the fossil fuel by country
    5. `get_coal`: get the coal consumption by country
9. Crime:
    1. `get_crime_rate`: get the crime rate by country
    2. `get_murder_rate`: get the murder rate by country
10. Immigration:
    1. `get_immigration_stats`: get the immigration statistics by country
    2. `get_net_migration`: get the net migration by country 
    3. `get_refugee_stats`: get the refugee statistics by country
11. Other:
    1. `get_military_spending`: get the military spending by country
    2. `get_military_size`: get the military size by country
    3. `get_suicide_rate`: get the suicide rate by country
    4. `get_edu_spending`: get the education spending by country
    5. `get_surface`: get the surface area by country
    6. `get_arable_land`: get the arable land by country