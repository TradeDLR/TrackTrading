import sys
sys.path.append('../TrackTrading') # Replace with the absolute path to your TrackTrading directory
from apiUtils import get_sign, send_request, parse_params
from FundBalance import get_coin_list_and_prices, calculation_usdt, debug
from csv_xlsx import write_to_csv

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
        # print(balances)
        Total_asset = calculation_usdt(balances, prices)
        debug(balances, Total_asset)
        write_to_csv(balances, Total_asset)
        print("Data has been written to output.csv")
    except Exception as e:
        print(f"Error occurred: {e}")