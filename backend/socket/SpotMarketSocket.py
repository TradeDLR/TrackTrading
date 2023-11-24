
from backend.market.spotinfo import SpotInfo
from backend.utils.utilities import PrintCommand
import time

class SpotMarketSocket(SpotInfo, PrintCommand):
    def __init__(self):
        # super().__init__()  # Initialize the parent class (PerpetualInfo)
        SpotInfo.__init__(self)
        commands = {
            ("price", "p"): self.spotPrice,
            ("candlestick", "c"): self.candlestickChart,
            ("symbols", "s"): self.querySymbols,
            ("depth", "d"): self.depthInfo,
            ("transaction", "t"): self.transactionRecords
            # ("quit", "q"): self.quit
        }

        descriptions = {
            "price (p)": "Get latest price and 24-hour price changes",
            "candlestick (c)": "Get candlestick chart data",
            "symbols (s)": "Get symbols info",
            "depth (d)": "Get market depth",
            "transaction (t)": "Get latest transaction",
            "quit (Q or q)": "Quit"
        }

        PrintCommand.__init__(self, commands, descriptions)

    def spotPrice(self):
        coin = self.coinInput()
        datas = self.getPrice(coin)
        if isinstance(coin, list):
            results = {}
            for c in coin:
                 if c in datas:
                    info = datas[c]
                    last_price = info['data'][0]['lastPrice']
                    percentage_change = ((last_price - info['data'][0]['openPrice']) / info['data'][0]['openPrice']) * 100
                    formatted_change = f"{percentage_change:.2f}% in 24hr"
                    results[c] = {'lastPrice': last_price, 'change': formatted_change}
            print(f"{results}")
        else:
            print("False")

    def depthInfo(self):
        coin = self.coinInput()
        limit = int(input("Optional value [1~100] : "))
        datas = self.getDepthInfo(coin, limit)
        n = 0
        if isinstance(coin, list):
            # print(f"{datas}")
            for n in range(limit):
                results = {}
                for c in coin:
                    if c in datas:
                        info = datas[c]
                        bid_price = info['data']['bids'][n][0]
                        bid_qty = info['data']['bids'][n][1]
                        ask_price = info['data']['asks'][n][0]
                        ask_qty = info['data']['asks'][n][1]

                        results[c] = {'bid price': bid_price, 'bid qty': bid_qty, 'ask price': ask_price, 'ask_qty': ask_qty}
                print(f"{results}")
        else:
            print("False")

    def transactionRecords(self):
        coin = self.coinInput()
        limit = int(input("Number : "))
        datas = self.getTransactionRecords(coin, limit=limit)
        n = 0
        if isinstance(coin, list):
            #print(f"{datas}")
            for n in range(limit):
                results = {}
                for c in coin:
                    if c in datas:
                        info = datas[c]
                        ID = info['data'][n]['id']
                        Price = info['data'][n]['price']
                        Qty = info['data'][n]['qty']
                        results[c] = {'ID': ID, 'Price': Price, 'Qty': Qty}
                print(f"{results}")
        else:
            print("False")

    def querySymbols(self):
        coin = self.coinInput()
        symbols = self.getQuerySymbols(coin)
        if isinstance(coin, list):
            results = {}
            for c in coin:
                if c in symbols:
                    results[c] = symbols[c]
            print(f"{results}")
        else:
            print("False")

    def candlestickChart(self):
        coin = self.coinInput()
        interval = str(input("Optional interval : [15m,30m,1h,4h,1d,1w,1M] : "))
        limit = int(input("Limit : "))
        candledata = self.getCandleChart(coin, interval=interval, limit=limit)

        if isinstance(coin, list):
            #print(f"{candledata}")
            for n in range(limit):
                results = {}
                for coin, info in candledata.items():
                    if 'data' in info and info['data']:
                        data = info['data'][n]
                        close_price = data[4]
                        min_price = data[3]
                        max_price = data[2]
                        open_price = data[1]
                        percentage_change = ((close_price - open_price) / open_price) * 100
                        formatted_change = f"{percentage_change:.2f}% in {interval}"
                        results[coin] = {'close': close_price, 'open': open_price, 'max': max_price, 'min': min_price, 'change': formatted_change}
                    else:
                        print("False")
                print(f"{results}")
        else:
            print("False")

    def coinInput(self):
        while True:
            input_string = input("Enter coins (separated by space): ")
            if input_string:
                coins = input_string.upper().split()
                valid_coins = [coin for coin in coins if self.getQuerySymbols(coin) is not None]

                if valid_coins:
                    return valid_coins
                else:
                    print(
                        f"Please try again. Invalid coins: {', '.join(coins)}")
            else:
                print("No coins entered. Please try again.")

def getSpotMarketSocket():
    return SpotMarketSocket()