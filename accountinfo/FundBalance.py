from apiUtils import get_sign, send_request, parse_params

def get_coin_list_and_prices(balances):  # get coin list from the fund account and each coin's latest price
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
            # print(f"1 {unit} is equivalent to {last_price} USDT.")
    return coin_lst, coin_prices


def calculation_usdt(balances, prices):  # calculate total asset and each coin's asset
    Total = 0
    for balance in balances:
        # print(balance)
        asset = balance.get('asset', '')
        free_balance = float(balance.get('free', '0'))
        locked_balance = float(balance.get('locked', '0'))
        total_balance = free_balance + locked_balance

        # Store total_balance into the balance dictionary
        balance['free_balance'] = free_balance
        balance['locked_balance'] = locked_balance
        balance['total_balance'] = total_balance

        coin_value = 0
        if asset in prices:
            coin_value = total_balance * prices[asset]
            Total += coin_value
        balance['usdt_value'] = coin_value

    return Total

def debug(balances, Total_asset):
    print("asset-currency", "balance", "free", "locked", "value-in-usdt")
    for balance in balances:
        print(balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'], balance['usdt_value'])
    print("Total Asset (USDT)", "", "", "", Total_asset)
