import time
import requests
import hmac
from hashlib import sha256
import sys
sys.path.append('../')

import config

class BingxAPI:
    APIURL = "https://open-api.bingx.com"
    APIKEY = config.API_KEY
    SECRETKEY = config.SECRET_KEY

    @staticmethod
    def getSign(api_secret, payload):
        signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
        return signature

    @staticmethod
    def sendRequest(method, path, url_params, payload={}):
        signature = BingxAPI.getSign(BingxAPI.SECRETKEY, url_params)
        url = f"{BingxAPI.APIURL}{path}?{url_params}&signature={signature}"
        headers = {'X-BX-APIKEY': BingxAPI.APIKEY}
        response = requests.request(method, url, headers=headers, data=payload)
        return response.json()  # changed to return json directly

    @staticmethod
    def parseParams(params_map):
        sortedKeys = sorted(params_map.keys())
        paramsStr = "&".join([f"{key}={params_map[key]}" for key in sortedKeys])
        return f"{paramsStr}&timestamp={int(time.time() * 1000)}"
