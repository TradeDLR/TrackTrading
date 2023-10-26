import ccxt
import config

class StandardBalance:
    def __init__(self, exchange):
        self.exchange = exchange

    def getStdBalance(self, asset='USDT'):  # You can set a default asset or require it as an argument
        try:
            balance = self.exchange.fetch_balance({'standard': True})
            assetBalance = balance['total'].get(asset, 0)
            print(assetBalance)
            return assetBalance
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0, 0, 0  # Return zeros or None if you prefer, in case of an error

    def getStdUP(self):
        try:
            balance = self.exchange.fetch_balance({'standard': True})
            unrealizedProfit = balance['info'].get('unrealizedProfit', 0)
            print(unrealizedProfit)
            return unrealizedProfit
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0 # Return zeros or None if you prefer, in case of an error

    def getStdRP(self):
        try:
            balance = self.exchange.fetch_balance({'standard': True})
            realizedProfit = balance['info'].get('realizedProfit', 0)
            print(realizedProfit)
            return realizedProfit
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0 # Return zeros or None if you prefer, in case of an error

    def getStdTotal(self, asset='USDT'):
        try:
            balance = self.exchange.fetch_balance({'standard': True})
            assetBalance = balance['total'].get(asset, 0)
            unrealizedProfit = balance['info'].get('unrealizedProfit', 0)
            realizedProfit = balance['info'].get('realizedProfit', 0)
            print(assetBalance + unrealizedProfit + realizedProfit)
            return assetBalance + unrealizedProfit + realizedProfit
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0.0