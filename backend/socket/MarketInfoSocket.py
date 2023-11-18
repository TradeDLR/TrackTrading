
# import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.market.perpinfo import PerpInfo
from backend.utils.utilities import PrintCommand
import time

class MarketInfoSocket(PerpInfo, PrintCommand):
    def __init__(self):
        # super().__init__()  # Initialize the parent class (PerpetualInfo)
        PerpInfo.__init__(self)
        commands = {
            ("contract", "c"): self.contractInfo,
            ("price", "p"): self.latestPrice,
            ("depth", "d"): self.marketDepth,
            ("trade", "tr"): self.latestTrade,
            ("funding rate", "fr"): self.currentFundingRate,
            ("funding history", "fh"): self.fundingRateHistory,
            ("kline", "k"): self.kLines,
            ("interest", "i"): self.openInterest,
            ("ticker", "ti"): self.ticker,
            ("book ticker", "bt"): self.bookTicker
            #("quit", "q"): self.quit
        }

        descriptions = {
            "contract (c)": "Get contract info",
            "price (p)": "Get latest price",
            "depth (d)": "Get market depth",
            "trade (tr)": "Get latest trade",
            "funding rate (fr)": "Get current funding rate",
            "funding history (fh)": "Get funding rate history",
            "kline (k)": "Get K-lines",
            "interest (i)": "Get open interest",
            "ticker (ti)": "Get ticker",
            "book ticker (bt)": "Get book ticker",
            "quit (Q or q)": "Quit"
        }

        PrintCommand.__init__(self, commands, descriptions)

    def contractInfo(self):
        coin = self.coinInput()
        contract = self.getContractInfo(coin)
        if contract is not None:
            print(f"Contract info: {contract} ")
        else:
            print("Failed to get contract info.")

    def latestPrice(self):
        coin = self.coinInput()
        price = self.getLatestPrice(coin)
        if price is not None:
            print(f"Latest price: {price} USDT")
        else:
            print("Failed to get price.")

    def marketDepth(self):
        coin = self.coinInput()
        numOption = int(input("Optional value [5,10,20,50,100,500,1000] : "))
        depth = self.getMarketDepth(coin, numOption)
        if depth is not None:
            print(f"Market depth: {depth} ")
        else:
            print("Failed to fetch perpetual balance.")

    def latestTrade(self):
        coin = self.coinInput()
        num = int(input("Number : "))
        trades = self.getLatestTrade(coin, limit=num)
        if trades is not None:
            print(f"Trades : {trades} ")
        else:
            print("Failed to get trade.")

    def currentFundingRate(self):
        coin = self.coinInput()
        fundingRate = self.getCurrentFundingRate(coin)
        if fundingRate is not None:
            print(f" {fundingRate} ")
        else:
            print("Failed to get funding rate.")

    def fundingRateHistory(self):
        coin = self.coinInput()
        rateHistory = self.getFundingRateHistory(coin)
        if rateHistory is not None:
            print(f" {rateHistory} ")
        else:
            print("Failed to get funding rate history.")

    def kLines(self):
        coin = self.coinInput()
        options = str(input("Optional interval : [15m,30m,1h,4h,1d,1w,1M] : "))
        currentTime = int(time.time() * 1000)
        endTime = currentTime - 10000000
        limit = int(input("Limit : "))
        kline = self.getKLines(coin, options, endTime, currentTime, limit)
        if kline is not None and len(kline) > 0:
            for k in kline:
                print(f"Open: {k[0]}, Close: {k[1]}, High: {k[2]}, Low: {k[3]}, Volume: {k[4]}, Time: {k[5]}")
        else:
            print("Failed to get kline.")
        
    def openInterest(self):
        coin = self.coinInput()
        openInterest = self.getOpenInterest(coin)
        if openInterest is not None:
            print(f" {openInterest} ")
        else:
            print("Failed to get open interest.")

    def ticker(self):
        coin = self.coinInput()
        ticker = self.getTicker(coin)
        if ticker is not None:
            print(f"Price Change: {ticker[0]}")
            print(f"Price Change Percent: {ticker[1]}")
            print(f"Last Price: {ticker[2]}")
            print(f"Last Quantity: {ticker[3]}")
            print(f"High Price: {ticker[4]}")
            print(f"Low Price: {ticker[5]}")
            print(f"Open Price: {ticker[6]}")
        else:
            print("Failed to get ticker.")

    def bookTicker(self):
        coin = self.coinInput()
        bookTicker = self.getBookTicker(coin)
        if bookTicker is not None:
            print(f"purchasePrice: {bookTicker[0]}")
            print(f"purchaseQty: {bookTicker[1]}")
            print(f"sellPrice: {bookTicker[2]}")
            print(f"sellQty: {bookTicker[3]}")
        else:
            print("Failed to get ticker.")

    def coinInput(self):
        while True:
            coin = str(input("Enter coin: ").upper())
            if coin:
                # Check if the coin exists
                if self.getContractInfo(coin) is not None:
                    return coin
                else:
                    print(f"{coin} is not a valid coin. Please try again.")
            else:
                print("No coin entered. Please try again.")

def getMarketInfoSocket():
    return MarketInfoSocket()

# if __name__ == "__main__":
#     user = MarketInfoSocket()
#     user.userInput()
