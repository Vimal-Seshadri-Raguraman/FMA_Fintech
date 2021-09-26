import Credentials as cred
import requests
from Resources import *

class Account:
    def __init__(self):
        self.__base_endpoint = 'account'
        self.__secret_key = cred.get_env_var("secret_key")
        self.__public_key = cred.get_env_var("public_key")
        self.base_url = IEX_BASE_URL

    def get(self, data='usage',**kwargs):
        if 'type' in kwargs.keys():
            url = f'{self.base_url}/{self.__base_endpoint}/{data}/{kwargs["type"]}?token{self.__secret_key}'
        else:
            url = f'{self.base_url}/{self.__base_endpoint}/{data}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return response

    def get_public_key(self):
        return self.__public_key

    def get_secret_key(self):
        return self.__secret_key