import time
import os
import requests
import pandas as pd

class PolygonStocksApiInformation():

    def __init__(self, api_key, provider=None, market=None, section=None):
        self.provider = provider
        self.market = market
        self.section = section
        self.api_key = api_key

    #======================
    # TICKERS
    #======================
    
    # ALL TICKERS
    def stocks_all_tickers(self, active="true", order = "asc", limit=1000, sort = "ticker"):
        
        url = f"https://api.polygon.io/v3/reference/{self.section}"
        params = {
            "market": self.market,
            "active": active, 
            "order": order,
            "limit": limit,
            "sort": sort,
            "apiKey": self.api_key
        }
        return url, params
    
    
    # TICKERS OVERVIEW
    def stocks_tickers_overview(self, ticker="AAPL", active="true", order = "asc", limit=1000, sort = "ticker"):

        url = f"https://api.polygon.io/v3/reference/tickers/{ticker}"
        params = {
            "market": self.market,
            "active": active, 
            "order": order,
            "limit": limit,
            "sort": sort,
            "apiKey": self.api_key
        }
        return url, params
    
    # TICKER TYPES
    def stocks_tickers_types(self, locale = "us", limit = 1000):

        url = f"https://api.polygon.io/v3/reference/tickers/"
        params = {
            "asset_class": self.market,
            "locale": locale,
            "limit": limit,
            "apiKey": self.api_key

        }
        return url, params
    
    def stocks_tickers_related(self, ticker="AAPL", active="true", order = "asc", limit=1000, sort = "ticker"):

        url = f"https://api.polygon.io/v1/related-companies/{ticker}"
        params = {
            "market": self.market,
            "active": active, 
            "order": order,
            "limit": limit,
            "sort": sort,
            "apiKey": self.api_key
        }
        return url, params
    
    #======================
    # DIVIDENDS
    #======================
    
    def stocks_dividends(self):
        url = f"https://api.polygon.io/v3/reference/{self.section}"
        params = {
            "order": 'asc',
            "limit": 1000,
            "sort": "ex_dividend_date",
            "apiKey": self.api_key

        }
        return url, params
    