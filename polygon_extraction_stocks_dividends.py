import time
import sys
import os
import requests
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime
from utils.funcs import  polygon_api_extraction, save_file
from utils.api_information import PolygonStocksApiInformation


provider = "polygon"
market = "stocks"
section = "dividends"

PATH_PROJECT = os.path.join(os.getcwd())
PATH_DATA = os.path.join(PATH_PROJECT,"data", provider)
current_date = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
path_file_name = os.path.join(PATH_DATA, f"{provider}__{market}_{section}_{current_date}.json")

load_dotenv()
polygon_api_key = os.getenv("POLYGON_API_KEY")

polygon_api_information = PolygonStocksApiInformation(polygon_api_key,
                                                provider = provider,
                                                market =  market,
                                                section =  section)
url, params =  polygon_api_information.stocks_dividends()

df = polygon_api_extraction(url, params)
save_file(df, path_file_name)