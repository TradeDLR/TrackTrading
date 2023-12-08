from backend.utils.apiUtils import getBingxAPI
from backend.market.spotinfo import getSpotInfo


class FundBalance:
    def __init__(self):
        self.bingxAPI = getBingxAPI()
        self.spotinfo = getSpotInfo()
        self.balances = []
        self.coinPrices = {}

    def getAssetData(self):
        return self.bingxAPI.fetchMarketData('spot/v1/account/balance').get('data', {}).get('balances', [])

    def getFundBalance(self):
        balance = self.getAssetData()
        self.balances = [b for b in balance if float(b['free']) != 0.0 or float(b['locked']) != 0.0]
        self.updateCoinPrices()
        fundTotal = self.calculationUSDT
        print(f"Possessing Monetary Value: {fundTotal}")
        print(f"Balance: {self.balances}")
        return fundTotal

    def getOwnCoin(self):
        return [balance.get('asset') for balance in self.balances if float(balance['free']) != 0.0 or float(balance['locked']) != 0.0]

    def getUsdtFree(self):
        balance = self.getAssetData()
        for b in balance:
            asset = b.get('asset')
            if asset == "USDT":
                freeBalance = float(b.get('free', '0'))
                return freeBalance

    def getCoinPrice(self, coins):
        for coin in coins:
            if coin == "USDT":
                self.coinPrices[coin] = 1.0
            else:
                price = self.spotinfo.getLastprice(coin)
                self.coinPrices[coin] = price
        return self.coinPrices

    def updateCoinPrices(self):
        coinList = self.getOwnCoin()
        self.getCoinPrice(coinList)
        print("Current Prices of Owned Coins", self.coinPrices)

    @property
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
                #print(f"{totalBalance}")
                #print(f"{self.coinPrices[asset]}")
                coinValue = totalBalance * self.coinPrices[asset]
                #print(f"Coin value: {coinValue}")
                total += coinValue
            balance['usdt_value'] = coinValue

        return total

    def debug(self, totalAsset):
        print("asset-currency", "balance", "free", "locked", "value-in-usdt")
        for balance in self.balances:
            print(balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                  balance['usdt_value'])
        print("Total Asset (USDT)", "", "", "", totalAsset)

def getFundBalance():
    return FundBalance()

#fund = FundBalance()
#fund.getUsdtFree()
