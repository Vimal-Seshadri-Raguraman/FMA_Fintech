import Credentials as cred
import requests
from Resources import *

class News:
    def __init__(self, symbol):
        self.symbol = symbol
        self.__public_key = cred.get_env_var("public_key")

    def news(self, last=None):
        """
        Provides intraday news from over 3,000 global news sources including major publications,
        regional media, and social. This function returns upto the last 50 articles. Use the
        historical news function to fetch news as far back as January 2019

        Credit Usage: 1 per symbol per news item returned
        Data Timing: Intraday
        Data Schedule: Continuous

        :param last: Number between 1 and 50. Default is 10
        :return:
        """
        endpoint = f'/stock/{self.symbol}/news'
        if last is not None:
            endpoint += f'/last/{last}?'
        else:
            endpoint += f'?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def streaming_News(self):
        """
        Not created yet.
        :return:
        """
        pass

    def historical_news(self, **kwargs):
        """
        Historical news from January 2019 forward. Uses the time series endpoint to provide news
        across the market or by symbol using any type of supported range.
        :param kwargs:
        :return:
        """
        endpoint = f'/time-series/news/{self.symbol}?'
        if len(kwargs.keys()) != 0:
            for key in kwargs.keys():
                endpoint += f'{key}={kwargs[key]}&'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response