import ccxt
import config

class StandardBalance:
    def __init__(self, exchange):
        self.exchange = exchange

    def get_std_balance(self, asset='USDT'):  # You can set a default asset or require it as an argument
        try:
            balance = self.exchange.fetch_balance({'standard': True})
            asset_balance = balance['total'].get(asset, 0)
            unrealized_profit = balance['info'].get('unrealizedProfit', 0)
            realized_profit = balance['info'].get('realizedProfit', 0)

            return asset_balance, unrealized_profit, realized_profit
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0, 0, 0  # Return zeros or None if you prefer, in case of an error

