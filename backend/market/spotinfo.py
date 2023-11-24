from backend.utils.apiUtils import getBingxAPI
import time
import datetime


class SpotInfo:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def getQuerySymbols(self, coin):
        return self.bingxAPI.fetchMarketData('spot/v1/common/symbols', coin)
        # symbols = self.bingxAPI.fetchMarketData('spot/v1/common/symbols').get('data', {}).get('symbols', [])
        # symbol = coin + "-USDT"
        # spot = next((s for s in symbols if s['symbol'] == symbol), None)
        # return spot  # self.bingxAPI.fetchMarketData('spot/v1/common/symbols')

    def getTransactionRecords(self, coin: str, limit: int = 0):
        return self.bingxAPI.fetchMarketData('spot/v1/market/trades', coin, limit=limit)

    def getDepthInfo(self, coin: str, limit: int = 0):
        return self.bingxAPI.fetchMarketData('spot/v1/market/depth', coin, method="GET",  limit=limit)

    def getCandleChart(self, coin: str, interval: str, startTime: int = 0, endTime: int = 0, limit: int = 0):
        response = self.bingxAPI.fetchMarketData('spot/v2/market/kline', coin, interval=interval, limit=limit)
        return response

    def getPrice(self, coin):
        response = self.bingxAPI.fetchMarketData('spot/v1/ticker/24hr', coin)
        return response

def getSpotInfo():
    return SpotInfo()



spotinfo = SpotInfo()

#coin = ["BTC", "ETH"]
coin = "BTC"
currentTime = int(time.time() * 1000)
fiveSecondAgo = currentTime - 5000000

print(spotinfo.getQuerySymbols(coin))
#print(spotinfo.getTransactionRecords(coin, 1))
#print(spotinfo.getDepthInfo(coin, 2))
#print(spotinfo.getCandleChart(coin, "1m", limit=2))
#print(spotinfo.getPrice(coin))
