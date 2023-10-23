import time
import requests
import hmac
from hashlib import sha256
import config

APIURL = "https://open-api.bingx.com"
APIKEY = config.API_KEY
SECRETKEY = config.SECRET_KEY

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    return signature


def send_request(method, path, url_params, payload):
    signature = get_sign(SECRETKEY, url_params)
    url = f"{APIURL}{path}?{url_params}&signature={signature}"
    headers = {'X-BX-APIKEY': APIKEY}
    response = requests.request(method, url, headers=headers, data=payload)
    return response


def parse_params(params_map):
    sortedKeys = sorted(params_map.keys())
    paramsStr = "&".join([f"{key}={params_map[key]}" for key in sortedKeys])
    return f"{paramsStr}&timestamp={int(time.time() * 1000)}"