import time
import os
import requests
import pandas as pd

class PolygonApiInformation():

    def __init__(self, api_key, provider=None, market=None, section=None):
        self.provider = provider
        self.market = market
        self.section = section
        self.api_key = api_key

    
    
    def stocks_tickers(self):
        url = f"https://api.polygon.io/v3/reference/{self.section}"
        params = {
            "market": self.market,
            "active": "true", 
            "order": "asc",
            "limit": 1000,
            "sort": "ticker",
            "apiKey": self.api_key
        }
        return url, params
    
    def stocks_dividends(self):
        url = f"https://api.polygon.io/v3/reference/{self.section}"
        params = {
            "order": 'asc',
            "limit": 1000,
            "sort": "ex_dividend_date",
            "apiKey": self.api_key

        }
        return url, params
    
    def stocks_tickers_types(self):

        url = f"https://api.polygon.io/v3/reference/tickers/{self.section}"
        params = {
            "asset_class": self.market,
            "locale": "us",
            "limit": 1000,
            "apiKey": self.api_key

        }
        return url, params


def polygon_api_extraction(url, params):
    res_ok = False
    while res_ok is False:
        response = requests.get(url, params=params)
        
        if response.status_code == 429:
            print("Too many requests, waiting 60s...")
            time.sleep(60)
            continue
        
        data = response.json()
        
        if "results" in data and len(data["results"]) > 0:
            data = data
            df = pd.DataFrame(data["results"])
            res_ok = True
        else:
            print("No results yet, retrying in 10s...")
            time.sleep(10)
    return df


def save_file(df,path_data):
    df.to_json(path_data)