#https://bingx-api.github.io/docs/#/swapV2/trade-api.html%23Trade%20order%20test

from accountinfo.apiUtils import BingxAPI
import time

class marketinfo:
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
        price = self.fetchMarketData("v2/quote/trades", coin, limit=limit)#.get("data", {}).get("price", "")
        # qty = self.fetchMarketData("v2/quote/trades", coin, limit=limit).get("data", {}).get("qty", "")
        return price

    def getCurrentFundingRate(self, coin: str):
        return self.fetchMarketData("v2/quote/premiumIndex", coin)

    def getFundingRateHistory(self, coin: str, start: int = 0, end: int = 0, limit: int = 0):
        return self.fetchMarketData("v2/quote/fundingRate", coin, start=start, end=end, limit=limit)

    def getKLines(self, coin: str, interval: str, start: int = 0, end: int = 0, limit: int = 0):
        return self.fetchMarketData("v3/quote/klines", coin, interval=interval, start=start, end=end, limit=limit)

    def getOpenInterest(self, coin: str):
        return self.fetchMarketData("v2/quote/openInterest", coin)

    def getTicker(self, coin: str):
        return self.fetchMarketData("v2/quote/ticker", coin)

    def getBookTicker(self, coin: str):
        return self.fetchMarketData("v2/quote/bookTicker", coin)




mar = marketinfo()
crypto_coin = "BTC"
currentTime = int(time.time() * 1000)
oneSecondAgo = currentTime - 1000

# print("1", mar.getContractInfo("BTC"))
print("LatestPrice :", mar.getLatestPrice(crypto_coin))
print("MarketDept :", mar.getMarketDepth(crypto_coin, 5))
print("LatestTrade :", mar.getLatestTrade(crypto_coin, limit=1))
print("CurrentFundingRate :", mar.getCurrentFundingRate(crypto_coin))
print("FundingRateHistory :", mar.getFundingRateHistory(crypto_coin, start=oneSecondAgo, end=currentTime, limit=1))
print("KLines :", mar.getKLines(crypto_coin, "4h", start=oneSecondAgo, end=currentTime, limit=3))
print("OpenInterest :", mar.getOpenInterest(crypto_coin))
print("Ticker :", mar.getTicker(crypto_coin))
print("BookTicker :", mar.getBookTicker(crypto_coin))
