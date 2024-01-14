import time
from collections import deque
from datetime import datetime
from backend.market.spotinfo import SpotInfo

class Notify(SpotInfo):
    def check_prices_and_notify(self, coins, check_interval=6, price_change_interval=30):
        """
        Continuously check the prices and print the percentage change every six seconds compared
        to the price three minutes ago.
        :param coins: A list of coins to monitor.
        :param check_interval: Time in seconds between each price check (6 seconds).
        :param price_change_interval: Time in seconds over which to measure price change (180 seconds for 3 minutes).
        """
        price_history = {coin: deque(maxlen=price_change_interval // check_interval) for coin in coins}
        max_coin_name_length = max(len(coin) for coin in coins)
        max_price_length = 0
        while True:
            for coin in coins:
                current_price = self.getLastprice(coin)
                current_time = datetime.now()
                price_str = f"{current_price:.10g}"  # Convert the price to string with general format
                max_price_length = max(max_price_length, len(price_str))

                # Maintain a rolling record of the last 3 minutes of prices
                price_history[coin].append((current_price, current_time))

                if len(price_history[coin]) == price_history[coin].maxlen:
                    # Compare current price to the price from 3 minutes ago
                    initial_price, initial_time = price_history[coin][0]

                    if initial_price:

                        change = (current_price - initial_price) / initial_price
                        price_str = f"{current_price:.10g}"
                        #print(f"{coin} Price Change Rate: {change * 100:.2f}%")
                        print(f"{coin.ljust(max_coin_name_length)} Price: {price_str.rjust(max_price_length)} - 3 min Change Rate: {change * 100:>6.2f}%")

            print(f"--------------{current_time.strftime('%Y-%m-%d %H:%M:%S')}--------------")
            time.sleep(check_interval)

# Example usage
# Assume 'self' has been defined in your class with the 'getLastprice' method
your_class_instance = Notify()
check_prices_and_notify = (['BTC','ETH','MUBI','APE'])
your_class_instance.check_prices_and_notify(check_prices_and_notify)
