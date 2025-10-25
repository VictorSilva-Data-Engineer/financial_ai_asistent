import time
import sys
import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from utils.funcs import polygon_api_extraction, save_file
from utils.api_information import  PolygonStocksApiInformation

load_dotenv()
polygon_api_key = os.getenv("POLYGON_API_KEY")

provider = "polygon"
market = "stocks"



PATH_PROJECT = os.path.join(os.getcwd())
PATH_DATA = os.path.join(PATH_PROJECT,"data", provider)
current_date = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

section_ticker = "tickers"
polygon_api_information = PolygonStocksApiInformation(polygon_api_key,
                                                provider = provider,
                                                market= market,
                                                section = section_ticker)

# ===========
# ALL TICKERS
# ===========


path_file_name_all_tickers = os.path.join(PATH_DATA, f"{provider}__{market}_all_{section_ticker}_{current_date}.json")
url_all_tickers, params_all_tickers =  polygon_api_information.stocks_all_tickers()
df_all_tickers = polygon_api_extraction(url_all_tickers, params_all_tickers)
save_file(df_all_tickers,  path_file_name_all_tickers)


# ===========
# TICKER OVERVIEW
# ===========

path_file_name_ticker_overview = os.path.join(PATH_DATA, f"{provider}__{market}_{section_ticker}_overview_{current_date}.json")

url_ticker_overview, params_ticker_overview =  polygon_api_information.stocks_tickers_overview()

df_ticker_overview = polygon_api_extraction(url_ticker_overview, params_ticker_overview)
save_file(df_ticker_overview,  path_file_name_ticker_overview)

# ===========
# TICKERS TYPES
# ===========

path_file_name_ticker_types= os.path.join(PATH_DATA, f"{provider}__{market}_{section_ticker}_{current_date}.json")

url_ticker_types, params_ticker_types =  polygon_api_information.stocks_tickers_types()

df_ticker_types = polygon_api_extraction(url_ticker_types, params_ticker_types)
save_file(df_ticker_types,  path_file_name_ticker_types)


# ===========
# TICKERS RELATED
# ===========

path_file_name_ticker_related = os.path.join(PATH_DATA, f"{provider}__{market}_related_{section_ticker}_{current_date}.json")

url_ticker_related, params_ticker_related =  polygon_api_information.stocks_tickers_related()

df_ticker_realted = polygon_api_extraction(url_ticker_related, params_ticker_related)
save_file(df_ticker_realted,  path_file_name_ticker_related)

time.sleep(60)

