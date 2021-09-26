from Resources import *
import requests

class MarketInfo:
    def __init__(self, symbol, key):
        self.symbol = symbol
        self.__public_key = key
        # /stock/{symbol}/advanced-stats

    def collections(self, collectionType, **kwargs):
        endpoint = f'/stock/market/collection/{collectionType}?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def earnings_today(self):
        endpoint = f'/stock/market/today-earnings?'
        url = IEX_BASE_URL+endpoint+f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def ipo_calendar(self, ipo_type='upcoming'):
        endpoint = f'/stock/market/{ipo_type}-ipos?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def list(self, list_type, **kwargs):
        endpoint = f'/stock/market/list/{list_type}?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def Market_Volume(self, **kwargs):
        endpoint = f'/stock/market/volume?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def sector_performance(self):
        endpoint = f'/stock/market/sector-performance?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def upcoming_events(self):
        raise NotImplementedError