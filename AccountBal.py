import time
import requests
import hmac
from hashlib import sha256
import csv
import config

APIURL = "https://open-api.bingx.com"
APIKEY = config.API_KEY
SECRETKEY = config.SECRET_KEY

def demo():
    try:
        path = '/openApi/spot/v1/account/balance'
        method = "GET"
        paramsMap = {
            "recvWindow": 0
        }
        paramsStr = parse_params(paramsMap)
        response = send_request(method, path, paramsStr, {})

        # Assuming the response is a JSON string, converting it to a dictionary
        response_dict = response.json()
        write_to_csv(response_dict)
        output(response_dict)
        return "Data has been written to output.csv"
    except Exception as e:
        return f"Error occurred: {e}"


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


def write_to_csv(data):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')

        # Writing the header
        writer.writerow(["asset-currency", "balance", "locked"])

        balances = data.get('data', {}).get('balances', [])
        for balance in balances:
            asset = balance.get('asset', '')
            free_balance = float(balance.get('free', '0'))
            locked_balance = float(balance.get('locked', '0'))
            total_balance = free_balance + locked_balance

            writer.writerow([asset, total_balance, locked_balance])

def output(data):
    balances = data.get('data', {}).get('balances', [])
    for balance in balances:
        asset = balance.get('asset', '')
        free_balance = float(balance.get('free', '0'))
        locked_balance = float(balance.get('locked', '0'))
        total_balance = free_balance + locked_balance

        print(asset, total_balance, locked_balance)

if __name__ == '__main__':
    print(demo())
