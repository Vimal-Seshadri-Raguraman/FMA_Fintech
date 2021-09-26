from Resources import *
import requests
import os
import Credentials as cred

def get(endpoint, **kwargs):
    url = IEX_BASE_URL + endpoint + f'token={cred.get_env_var("public")}'
    if "test" in kwargs.keys():
        if kwargs["test"]:
            url = IEX_SANDBOX_BASE_URL+endpoint+f'token={IEX_TEST_SECRET_KEY}'
    response = requests.get(url)
    return response