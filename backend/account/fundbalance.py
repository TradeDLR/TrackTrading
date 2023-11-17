from backend.utils.apiUtils import getBingxAPI
from backend.utils.csv_xlsx import AssetWriter


class FundBalance:
    def __init__(self):
        self.bingxAPI = getBingxAPI()
        self.balances = []
        self.coinPrices = {}

    def getFundBalance(self):
        balance = self.bingxAPI.fetchMarketData('spot/v1/account/balance').get('data', {}).get('balances', [])
        self.balances = [b for b in balance if float(b['free']) != 0.0 or float(b['locked']) != 0.0]
        # print(self.balances)
        self.updateCoinPrices()
        fundTotal = self.calculationUSDT()
        # print(f"Fund total: {fundTotal}")
        return fundTotal

    def getOwnCoin(self):
        return [balance.get('asset') for balance in self.balances if float(balance['free']) != 0.0 or float(balance['locked']) != 0.0]

    def getCoinPrice(self, coin):
        if coin == "USDT":
            return 1.0

        response = self.bingxAPI.fetchMarketData('spot/v1/ticker/24hr', coin)
        data = response.get('data', [])
        if data:
            return self.extractPrice(data)
        return None

    @staticmethod
    def extractPrice(data):
        # Assuming data[0] contains the required price info
        return float(data[0].get('lastPrice', 0))

    def updateCoinPrices(self):
        coinList = self.getOwnCoin()
        for coin in coinList:
            self.coinPrices[coin] = self.getCoinPrice(coin)
        print("Updated coin prices:", self.coinPrices)

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


# fund = FundBalance()
# fund.getFundBalance()