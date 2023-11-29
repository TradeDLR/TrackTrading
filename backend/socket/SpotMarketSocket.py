
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
        for c in coin:
            datas = self.getPrice(c)
            percentage_change = ((datas[3] - datas[0]) / datas[0]) * 100
            #formatted_change = f"{percentage_change:.2f}% in 24hr"
            print(f"<{c}> Open: {datas[0]}, High: {datas[1]}, Low: {datas[2]}, Last: {datas[3]}, Volume: {datas[4]}, Rate: {percentage_change:.2f}% in 24hr")

    def candlestickChart(self):
        coin = self.coinInput()
        interval = str(input("Optional interval : [3m,15m,30m,1h,4h,8h,1d,3d,1w,1M] : "))
        limit = int(input("Limit : "))
        for c in coin:
            datas = self.getCandleChart(c, interval=interval, limit=limit)
            for n in range(limit):
                percentage_change = ((datas[3][n] - datas[0][n]) / datas[0][n]) * 100
                print(f"<{c}> Open: {datas[0][n]}, Max: {datas[1][n]}, Min: {datas[2][n]}, Close: {datas[3][n]}, Rate: {percentage_change:.2f}% in {interval}")

    def querySymbols(self):
        coin = self.coinInput()
        for c in coin:
            datas = self.getQuerySymbols(c)
            print(f"{c} : {datas}")

    def depthInfo(self):
        coin = self.coinInput()
        limit = int(input("Optional value [1~100] : "))
        for c in coin:
            datas = self.getDepthInfo(c, limit)
            print(f"{c} : {datas}")

    def transactionRecords(self):
        coin = self.coinInput()
        limit = int(input("Number : "))
        for c in coin:
            datas = self.getTransactionRecords(c, limit)
            print(f"{c} : {datas}")

    def coinInput(self):
        while True:
            input_string = input("Enter coins (separated by space): ")
            if input_string:
                coins = input_string.upper().split()
                valid_coins = [coin for coin in coins if self.getQuerySymbols(coin) is not None]

                if valid_coins:
                    return valid_coins
                else:
                    print(f"Please try again. Invalid coins: {', '.join(coins)}")
            else:
                print("No coins entered. Please try again.")

def getSpotMarketSocket():
    return SpotMarketSocket()