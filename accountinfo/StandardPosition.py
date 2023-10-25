import ccxt
import config

class StandardPosition:
    def __init__(self):
        self.exchange = ccxt.bingx({
            'apiKey': config.API_KEY,
            'secret': config.SECRET_KEY,
        })

    def get_open_order(self):
        # You'll need to replace 'your_symbol' with the actual trading symbol you are interested in.
        open_orders = self.exchange.fetch_open_orders()
        total_margin = sum(order['info']['margin'] for order in open_orders)
        total_unrealized_profit = sum(order['info']['unrealized_profit'] for order in open_orders)
        return total_margin, total_unrealized_profit
