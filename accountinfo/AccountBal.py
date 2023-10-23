import time
import requests
import hmac
from hashlib import sha256
import csv
import sys
sys.path.append('../TrackTrading') # Replace with the absolute path to your TrackTrading directory

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


def get_coin_list_and_prices(balances):
    coin_lst = []
    coin_prices = {}
    path = '/openApi/spot/v1/ticker/24hr'
    method = "GET"
    for balance in balances:
        unit = balance.get('asset')
        coin_lst.append(unit)

        if unit == "USDT":
            coin_prices[unit] = 1.0
            continue

        symbol = unit + "-USDT"
        paramsMap = {
            "symbol": symbol
        }
        paramsStr = parse_params(paramsMap)
        response = send_request(method, path, paramsStr, {})
        data = response.json().get('data', [])
        if data:
            last_price = data[0].get('lastPrice', 0)
            coin_prices[unit] = last_price
            print(f"1 {unit} is equivalent to {last_price} USDT.")
    return coin_lst, coin_prices


def calculation_usdt(balances, prices):
    Total = 0
    for balance in balances:
        asset = balance.get('asset', '')
        free_balance = float(balance.get('free', '0'))
        locked_balance = float(balance.get('locked', '0'))
        total_balance = free_balance + locked_balance

        # Store total_balance into the balance dictionary
        balance['total_balance'] = total_balance
        balance['locked_balance'] = locked_balance

        coin_value = 0
        if asset in prices:
            coin_value = total_balance * prices[asset]
            Total += coin_value
        balance['usdt_value'] = coin_value

    return Total


def write_to_csv(balances, Total_asset):
    with open('accountinfo/output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["asset-currency", "balance", "locked", "value-in-usdt"])
        for balance in balances:
            writer.writerow([balance['asset'], balance['total_balance'], balance['locked_balance'], balance['usdt_value']])
        writer.writerow(["Total Asset (USDT)", "", "", Total_asset])


def debug(balances, Total_asset):
    print("asset-currency", "balance", "locked", "value-in-usdt")
    for balance in balances:
        print(balance['asset'], balance['total_balance'], balance['locked_balance'], balance['usdt_value'])
    print("Total Asset (USDT)", "", "", Total_asset)


if __name__ == '__main__':
    try:
        path = '/openApi/spot/v1/account/balance'
        method = "GET"
        paramsMap = {
            "recvWindow": 0
        }
        paramsStr = parse_params(paramsMap)
        response = send_request(method, path, paramsStr, {})
        response_dict = response.json()
        balances = response_dict.get('data', {}).get('balances', [])
        _, prices = get_coin_list_and_prices(balances)

        Total_asset = calculation_usdt(balances, prices)
        print(balances)
        write_to_csv(balances, Total_asset)
        # debug(balances, Total_asset)
        print("Data has been written to output.csv")
    except Exception as e:
        print(f"Error occurred: {e}")