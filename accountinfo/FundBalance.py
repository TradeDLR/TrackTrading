from csv_xlsx import AssetWriter

class FundBalance:
    def __init__(self, exchange):
        self.exchange = exchange
        self.balances = []

    def getCoinListPrices(self, balances):
        coinPrices = {}
        for balance in balances:
            asset = balance.get('asset', 'Unknown Asset')
            if asset == "USDT":
                coinPrices[asset] = 1.0
            else:
                symbol = f"{asset}/USDT"
                if symbol in self.exchange.symbols:
                    ticker = self.exchange.fetch_ticker(symbol)
                    coinPrices[asset] = float(ticker['last'])
                else:
                    print(f"Warning: Symbol {symbol} not found in exchange symbols.")
        return coinPrices

    @staticmethod
    def getPrices(data, unit):
        lastPrice = data[0].get('lastPrice', 0)
        return lastPrice

    def calculationUSDT(self, balances, prices):
        total = 0
        for balance in balances:
            asset = balance['asset']
            totalBalance = balance['total_balance']
            if asset in prices:
                coinValue = totalBalance * prices[asset]
                total += coinValue
                balance['usdt_value'] = coinValue
            else:
                print(f"Warning: Price for {asset} not found. Setting 'usdt_value' to 0.")
                balance['usdt_value'] = 0
        return total

    @staticmethod
    def debug(balances, totalAsset):
        print("asset-currency", "balance", "free", "locked", "value-in-usdt")
        for balance in balances:
            usdtValue = balance.get('usdt_value', 'N/A')  # Default to 'N/A' if 'usdt_value' is missing
            print(balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                  usdtValue)
        print("Total Asset (USDT)", "", "", "", totalAsset)

    def getFundBalance(self):
        try:
            balance = self.exchange.fetch_balance()
            # balances = []
            for asset, amount in balance['total'].items():
                freeBalance = balance['free'][asset]
                if freeBalance != 0.0:
                    lockedBalance = balance['used'][asset]
                    totalBalance = freeBalance + lockedBalance
                    self.balances.append({
                        'asset': asset,
                        'free_balance': freeBalance,
                        'locked_balance': lockedBalance,
                        'total_balance': totalBalance,
                    })

            prices = self.getCoinListPrices(self.balances)
            fundTotal = self.calculationUSDT(self.balances, prices)
            # FundBalance.debug(balances, fundTotal)
            print(fundTotal)
            return fundTotal
        except Exception as e:
            print(f"Error occurred: {e}")
            
    def callCsvXlsx(self, fundTotal):
        writer = AssetWriter()
        writer.writeTotalAssetCSV(self.balances, fundTotal)


