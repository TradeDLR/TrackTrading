from apiUtils import get_sign, send_request, parse_params

def get_opened_order():
    path = '/openApi/contract/v1/allPosition'
    method = "GET"
    paramsMap = {
        "recvWindow": 0
    }
    paramsStr = parse_params(paramsMap)
    response = send_request(method, path, paramsStr, {})
    response_dict = response.json()
    print(response_dict)
    margin, unrealized_profit = get_margin_unrealized_profit(response_dict)

    return margin, unrealized_profit

def get_margin_unrealized_profit(dict):
    orders = dict.get('data', [])
    for order in orders:
        symbol = order.get('symbol', '')
        margin = order.get('initialMargin', 0)
        unrealized_profit = order.get('unrealizedProfit', 0)

        order["margin"] = margin
        order["unrealized_profit"] = unrealized_profit

    # print(order["margin"])
    # print(order["unrealized_profit"])
    return order["margin"], order["unrealized_profit"]