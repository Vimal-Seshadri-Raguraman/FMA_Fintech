from Resources import *
import requests

class Corporate_Action:
    def __init__(self, symbol, public_key):
        self.symbol = symbol
        self.__public_key = public_key
        pass