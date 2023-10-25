import ccxt
import config

class PerpetualBalance:
    def __init__(self):
        self.exchange = ccxt.bingx({
            'apiKey': config.API_KEY,
            'secret': config.SECRET_KEY,
        })

    def get_perp_balance(self):
        balance = self.exchange.fetch_balance()
        asset = balance['total']['USDT']  # Replace 'USDT' with the actual asset you are interested in.
        # Fetching unrealized and realized profits might need additional API calls or calculations depending on the exchange.
        unrealized_profit = 0  # Placeholder value
        realized_profit = 0  # Placeholder value
        return asset, unrealized_profit, realized_profit
