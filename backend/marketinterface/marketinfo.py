#https://bingx-api.github.io/docs/#/swapV2/trade-api.html%23Trade%20order%20test

from backend.accountinfo.apiUtils import BingxAPI
import time
import datetime

class MarketInfo:
    def __init__(self):
        self.bingxAPI = BingxAPI()

    def fetchMarketData(self, req: str, coin: str, interval: str = None, start: int = None, end: int = None, limit: int = None):
        payload = {}
        path = '/openApi/swap/' + req
        method = "GET"
        paramsMap = {"symbol": coin + "-USDT",
                     "interval": interval,
                     "startTime": start,
                     "endTime": end,
                     "limit": limit}
        paramsMap = {k: v for k, v in paramsMap.items() if v is not None}
        paramsStr = self.bingxAPI.parseParams(paramsMap)
        return self.bingxAPI.sendRequest(method, path, paramsStr, payload)

    def getContractInfo(self, coin: str):
        return self.fetchMarketData("v2/quote/contracts", coin)

    def getLatestPrice(self, coin: str):
        return self.fetchMarketData("v2/quote/price", coin).get("data", {}).get("price", "")

    def getMarketDepth(self, coin: str, limit: int = 0):  # limit: len=0|oneof=5 10 20 50 100 500 1000
        return self.fetchMarketData("v2/quote/depth", coin, limit=limit).get("data", {}).get("bids", [])

    def getLatestTrade(self, coin: str, limit: int = 1):
        data = self.fetchMarketData("v2/quote/trades", coin, limit=limit).get("data", [])
        for trade in data:
            price = trade.get("price")
            qty = trade.get("qty")
        return price, qty

    def getCurrentFundingRate(self, coin: str):
        fundingRate = self.fetchMarketData("v2/quote/premiumIndex", coin).get('data', {}).get('lastFundingRate', '')
        nextFundingTime = self.fetchMarketData("v2/quote/premiumIndex", coin).get('data', {}).get('nextFundingTime', '')
        timestamp_s = nextFundingTime / 1000
        date = datetime.datetime.fromtimestamp(timestamp_s)

        # print(date)
        return fundingRate, nextFundingTime, date

    def getFundingRateHistory(self, coin: str, start: int = 0, end: int = 0, limit: int = 0):

        return self.fetchMarketData("v2/quote/fundingRate", coin, start=start, end=end, limit=limit)

    def getKLines(self, coin: str, interval: str, start: int = 0, end: int = 0, limit: int = 0):
        #data = self.fetchMarketData("v3/quote/klines", coin, interval=interval, start=start, end=end, limit=limit).get('data', [])
        #for kbar in data:
        #    open = kbar.get('open')
        #    close = kbar.get('close')
        #    high = kbar.get('high')
        #    low = kbar.get('low')
        #    volume = kbar.get('volume')
        #    time = kbar.get('time')
        #    timestamp_s = time / 1000
        #    date = datetime.datetime.fromtimestamp(timestamp_s)

        #return open, close, high, low, volume, date
        data = self.fetchMarketData("v3/quote/klines", coin, interval=interval, start=start, end=end, limit=limit).get('data', [])
        fields = ["open", "close", "high", "low", "volume", "time"]
        return [tuple(kbar.get(field, '') if field != 'time' else datetime.datetime.fromtimestamp(kbar.get(field, 0) / 1000) for field in fields) for kbar in data]
    
    def getOpenInterest(self, coin: str):
        return self.fetchMarketData("v2/quote/openInterest", coin).get('data', {}).get('openInterest', '')

    def getTicker(self, coin: str):
        #priceChange = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('priceChange', '')
        #priceChangePercent = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('priceChangePercent', '')
        #lastPrice = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('lastPrice', '')
        #lastQty = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('lastQty', '')
        #highPrice = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('highPrice', '')
        #lowPrice = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('lowPrice', '')
        #openPrice = self.fetchMarketData("v2/quote/ticker", coin).get('data', {}).get('openPrice', '')
        #return priceChange, priceChangePercent, lastPrice, lastQty, highPrice, lowPrice, openPrice
        response = self.fetchMarketData("v2/quote/ticker", coin).get('data', {})
        fields = ["priceChange", "priceChangePercent", "lastPrice", "lastQty", "highPrice", "lowPrice", "openPrice"]
        return tuple(response.get(field, '') for field in fields)

    def getBookTicker(self, coin: str):
        #purchasePrice = self.fetchMarketData("v2/quote/bookTicker", coin).get("data", {}).get("book_ticker", {}).get("bid_price", '')
        #purchaseQty = self.fetchMarketData("v2/quote/bookTicker", coin).get("data", {}).get("book_ticker", {}).get("bid_qty", '')
        #sellPrice = self.fetchMarketData("v2/quote/bookTicker", coin).get("data", {}).get("book_ticker", {}).get("ask_price", '')
        #sellQty = self.fetchMarketData("v2/quote/bookTicker", coin).get("data", {}).get("book_ticker", {}).get("ask_qty", '')

        #return purchasePrice, purchaseQty, sellPrice, sellQty
        response = self.fetchMarketData("v2/quote/bookTicker", coin).get("data", {}).get("book_ticker", {})
        fields = ["bid_price", "bid_qty", "ask_price", "ask_qty"]
        return tuple(response.get(field, '') for field in fields)



# mar = MarketInfo()
# crypto_coin = "BTC"
# currentTime = int(time.time() * 1000)
# fiveSecondAgo = currentTime - 5000

# print("1", mar.getContractInfo("BTC"))
# print("LatestPrice", mar.getLatestPrice("crypto_coin"))
# print("MarketDept", mar.getMarketDepth("crypto_coin", 5))
# print("LatestTrade", mar.getLatestTrade("crypto_coin", limit=1))
# print("CurrentFundingRate", mar.getCurrentFundingRate("crypto_coin"))
# print("FundingRateHistory", mar.getFundingRateHistory("crypto_coin", start=fiveSecondAgo, end=currentTime, limit=0))
# print("KLines", mar.getKLines("crypto_coin", "4h", start=fiveSecondAgo, end=currentTime, limit=3))
# print("OpenInterest", mar.getOpenInterest("crypto_coin"))
# print("Ticker", mar.getTicker("crypto_coin"))
# print("BookTicker", mar.getBookTicker("crypto_coin"))
