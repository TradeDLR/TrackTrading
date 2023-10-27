import time
import requests
import hmac
from hashlib import sha256
import config


class BingxAPI:
    APIURL = "https://open-api.bingx.com"
    APIKEY = config.API_KEY
    SECRETKEY = config.SECRET_KEY

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({'X-BX-APIKEY': BingxAPI.APIKEY})

    def getSign(self, payload):
        signature = hmac.new(self.SECRETKEY.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
        return signature

    def sendRequest(self, method, path, urlParams, payload={}):
        signature = self.getSign(urlParams)
        url = f"{self.APIURL}{path}?{urlParams}&signature={signature}"
        response = self.session.request(method, url, data=payload)
        return response.json()

    @staticmethod
    def parseParams(paramsMap):
        sortedKeys = sorted(paramsMap.keys())
        paramsStr = "&".join([f"{key}={paramsMap[key]}" for key in sortedKeys])
        return f"{paramsStr}&timestamp={int(time.time() * 1000)}"
