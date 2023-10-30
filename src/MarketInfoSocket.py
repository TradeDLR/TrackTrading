from marketinterface import marketinfo
import time

class MarketInfoSocket:
    def __init__(self):
        self.mar = marketinfo.MarketInfo()

        self.commands = {
            "contract": self.ContractInfo,
            "price": self.LatestPrice,
            "depth": self.MarketDepth,
            "trade": self.LatestTrade,
            "funding_rate": self.CurrentFundingRate,
            "funding_history": self.FundingRateHistory,
            "kline": self.KLines,
            "interest": self.OpenInterest,
            "ticker": self.Ticker,
            "book_ticker": self.BookTicker,
            "quit": self.quit
        }

        self.descriptions = {
            "contract": "Get contract info",
            "price": "Get latest price",
            "depth": "Get market depth",
            "trade": "Get latest trade",
            "funding_rate": "Get current funding rate",
            "funding_history": "Get funding rate history",
            "kline": "Get K-lines",
            "interest": "Get open interest",
            "ticker": "Get ticker",
            "book_ticker": "Get book ticker",
            "quit": "Quit"
        }

    def ContractInfo(self):
        the_coin = self.coin_input()
        contract = self.mar.getContractInfo(the_coin)  
        if contract is not None:
            print(f"Contract info: {contract} ")
        else:
            print("Failed to get contract info.")

    def LatestPrice(self):
        the_coin = self.coin_input()
        price = self.mar.getLatestPrice(the_coin)
        if price is not None:
            print(f"Latest price: {price} USDT")
        else:
            print("Failed to get price.")

    def MarketDepth(self):
        the_coin = self.coin_input()
        num_option = int(input("Optional value [5,10,20,50,100,500,1000] : "))
        depth = self.mar.getMarketDepth(the_coin, num_option)
        if depth is not None:
            print(f"Market depth: {depth} ")
        else:
            print("Failed to fetch perpetual balance.")

    def LatestTrade(self):
        the_coin = self.coin_input()
        num = int(input("Number : "))
        trades = self.mar.getLatestTrade(the_coin, limit=num)
        if trades is not None:
            print(f"Trades : {trades} ")
        else:
            print("Failed to get trade.")

    def CurrentFundingRate(self):
        the_coin = self.coin_input()
        funding_rate = self.mar.getCurrentFundingRate(the_coin)
        if funding_rate is not None:
            print(f" {funding_rate} ")
        else:
            print("Failed to get funding rate.")

    def FundingRateHistory(self):
        the_coin = self.coin_input()
        rate_history = self.mar.getFundingRateHistory(the_coin)
        if rate_history is not None:
            print(f" {rate_history} ")
        else:
            print("Failed to get funding rate history.")

    def KLines(self):
        the_coin = self.coin_input()
        options = str(input("Optional interval : [15m,30m,1h,4h,1d,1w,1M] : "))
        currentTime = int(time.time() * 1000)
        endTime = currentTime - 10000000
        limit = int(input("Limit : "))
        kline = self.mar.getKLines(the_coin, options, endTime, currentTime, limit)
        if kline is not None:
            print(f" {kline} ")
        else:
            print("Failed to get kline.")
        
    def OpenInterest(self):
        the_coin = self.coin_input()
        open_interest = self.mar.getOpenInterest(the_coin)
        if open_interest is not None:
            print(f" {open_interest} ")
        else:
            print("Failed to get open interest.")

    def Ticker(self):
        the_coin = self.coin_input()
        the_ticker = self.mar.getTicker(the_coin)
        if the_ticker is not None:
            print(f" {the_ticker} ")
        else:
            print("Failed to get ticker.")

    def BookTicker(self):
        the_coin = self.coin_input()
        book_ticker = self.mar.getBookTicker(the_coin)
        if book_ticker is not None:
            print(f" {book_ticker} ")
        else:
            print("Failed to get ticker.")

    def quit(self):
        print("Goodbye")
        exit()

    def print_commands(self):
        print("*" * 56)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:10]) if len(command) > 15 else command.ljust(16)
            fixed_length_description = (description[:29]) if len(description) > 31 else description.ljust(32)
            print(f"* {fixedLengthCommand} -> {fixed_length_description} *")
        print("*" * 56)

    def user_input(self):
        while True:
            self.print_commands()
            user_command = input("Enter command: ").lower()
            if user_command == 'quit':
                break
            if user_command in self.commands:
                self.commands[user_command]()
            else:
                print("Unknown command. Please try again.")

    def coin_input(self):
        while True:
            crypto_coin = str(input("Enter coin: ").upper())
            if crypto_coin:
                return crypto_coin
            else:
                print("Unknown coin. Please try again.")

if __name__ == "__main__":
    user = MarketInfoSocket()
    user.user_input()
