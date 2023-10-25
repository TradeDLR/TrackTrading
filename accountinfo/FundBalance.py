from apiUtils import BingxAPI
from csv_xlsx import AssetWriter
class FundBalance(BingxAPI):
    @staticmethod
    def getCoinListPrices(balances):
        coinLst = []
        coinPrices = {}
        path = '/openApi/spot/v1/ticker/24hr'
        method = "GET"
        for balance in balances:
            unit = balance.get('asset')
            coinLst.append(unit)

            if unit == "USDT":
                coinPrices[unit] = 1.0
                continue
            symbol = unit + "-USDT"
            paramsMap = {
                "symbol": symbol
            }
            paramsStr = FundBalance.parseParams(paramsMap)
            response = FundBalance.sendRequest(method, path, paramsStr, {})
            data = response.get('data', [])
            if data:
                coinPrices[unit] = FundBalance.getPrices(data, unit)
        return coinLst, coinPrices

    @staticmethod
    def getPrices(data, unit):
        lastPrice = data[0].get('lastPrice', 0)
        return lastPrice

    @staticmethod
    def calculationUSDT(balances, prices):
        Total = 0
        for balance in balances:
            asset = balance.get('asset', '')
            free_balance = float(balance.get('free', '0'))
            locked_balance = float(balance.get('locked', '0'))
            total_balance = free_balance + locked_balance

            balance['free_balance'] = free_balance
            balance['locked_balance'] = locked_balance
            balance['total_balance'] = total_balance

            coin_value = 0
            if asset in prices:
                coin_value = total_balance * prices[asset]
                Total += coin_value
            balance['usdt_value'] = coin_value

        return Total

    @staticmethod
    def debug(balances, Total_asset):
        print("asset-currency", "balance", "free", "locked", "value-in-usdt")
        for balance in balances:
            print(balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'], balance['usdt_value'])
        print("Total Asset (USDT)", "", "", "", Total_asset)

    @staticmethod
    def getFundBalance():
        try:
            path = '/openApi/spot/v1/account/balance'
            method = "GET"
            paramsMap = {
                "recvWindow": 0
            }
            balances = FundBalance.getBalance(path, method, paramsMap)
            # for balance in balances:
            #     print("Asset:", balance['asset'])
            #     print("Free (type):", type(balance['free']))
            #     print("Free (value):", balance['free'])

            filtered_balances = [b for b in balances if float(b['free']) != 0.0]
            # print("filtered_balances: ", filtered_balances)
            _, prices = FundBalance.getCoinListPrices(filtered_balances)
            fundTotal = FundBalance.calculationUSDT(filtered_balances, prices)
            writer = AssetWriter()
            writer.writeTotalAssetCSV(filtered_balances, fundTotal)
            return fundTotal
        except Exception as e:
            print(f"Error occurred: {e}")

    @staticmethod
    def getBalance(path, method, parMap):
        paramsStr = FundBalance.parseParams(parMap)
        responseDict = FundBalance.sendRequest(method, path, paramsStr)
        return responseDict.get('data', {}).get('balances', [])
