from Resources import *
import requests

class Cryptocurrency:
    def __init__(self, symbol, public_key):
        self.symbol = symbol
        self.__public_key = public_key

    def cryptocurrency_book(self, streaming:bool):
        if streaming:
            endpoint = f'/cryptoBook?symbols={self.symbol}&token={self.__public_key}'
            url = IEX_STREAMING_URL+endpoint
            response = requests.get(url)
            return response
        else:
            endpoint = f'/crypto/{self.symbol}/book?'
            url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
            response = requests.get(url)
            return response

    def cryptocurrency_event(self):
        endpoint = f'cryptoEvents?symbols={self.symbol}&token={self.__public_key}'
        url = IEX_STREAMING_URL+endpoint
        response = requests.get(url)
        return response

    def cryptocurrency_price(self):
        endpoint = f'/crypto/{self.symbol}/price?'
        url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
        response = requests.get(url)
        return response

    def cryptocurrency_quote(self, streaming: bool):
        if streaming:
            endpoint = f'/cryptoQuotes?symbols={self.symbol}&token={self.__public_key}'
            url = IEX_STREAMING_URL + endpoint
            response = requests.get(url)
            return response
        else:
            endpoint = f'/crypto/{self.symbol}/quote?'
            url = IEX_BASE_URL + endpoint + f'token={self.__public_key}'
            response = requests.get(url)
            return response