from .apiUtils import BingxAPI
from .csv_xlsx import AssetWriter


class FundBalance:
    def __init__(self):
        self.balances = []
        self.bingxAPI = BingxAPI()
        self.coinPrices = {}

    def getCoinListPrices(self):
        coinList = []
        path = '/openApi/spot/v1/ticker/24hr'
        method = "GET"
        for balance in self.balances:
            unit = balance.get('asset')
            coinList.append(unit)

            if unit == "USDT":
                self.coinPrices[unit] = 1.0
                continue
            symbol = unit + "-USDT"
            paramsMap = {"symbol": symbol}
            paramsStr = self.bingxAPI.parseParams(paramsMap)
            response = self.bingxAPI.sendRequest(method, path, paramsStr, {})
            data = response.get('data', [])
            if data:
                self.coinPrices[unit] = self.getPrices(data, unit)
        return coinList

    @staticmethod
    def getPrices(data, unit):
        lastPrice = data[0].get('lastPrice', 0)
        return lastPrice

    def calculationUSDT(self):
        total = 0
        for balance in self.balances:
            asset = balance.get('asset', '')
            freeBalance = float(balance.get('free', '0'))
            lockedBalance = float(balance.get('locked', '0'))
            totalBalance = freeBalance + lockedBalance

            balance['free_balance'] = freeBalance
            balance['locked_balance'] = lockedBalance
            balance['total_balance'] = totalBalance

            coinValue = 0
            if asset in self.coinPrices:
                coinValue = totalBalance * self.coinPrices[asset]
                total += coinValue
            balance['usdt_value'] = coinValue

        return total

    def debug(self, totalAsset):
        print("asset-currency", "balance", "free", "locked", "value-in-usdt")
        for balance in self.balances:
            print(balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                  balance['usdt_value'])
        print("Total Asset (USDT)", "", "", "", totalAsset)

    def getFundBalance(self):
        try:
            path = '/openApi/spot/v1/account/balance'
            method = "GET"
            paramsMap = {"recvWindow": 0}
            self.balances = self.getBalance(path, method, paramsMap)
            self.balances = [b for b in self.balances if float(b['free']) != 0.0]  # filter and store in self.balances

            self.getCoinListPrices()
            fundTotal = self.calculationUSDT()

            print(fundTotal)
            return fundTotal
        except Exception as e:
            print(f"Error occurred: {e}")

    def getBalance(self, path, method, parMap):
        paramsStr = self.bingxAPI.parseParams(parMap)
        responseDict = self.bingxAPI.sendRequest(method, path, paramsStr)
        return responseDict.get('data', {}).get('balances', [])

    def callCsvXlsx(self, fundTotal):
        writer = AssetWriter()
        writer.writeTotalAssetCSV(self.balances, fundTotal)
