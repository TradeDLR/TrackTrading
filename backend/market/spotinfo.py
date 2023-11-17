from backend.utils.apiUtils import getBingxAPI
import time
import datetime

class SpotInfo:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def getQuerySymbols(self, coin: str):
        return self.bingxAPI.fetchMarketData('spot/v1/common/symbols', coin)

    def getTranscationRecords(self, coin: str, limit: int = 2):
        return self.bingxAPI.fetchMarketData('spot/v1/market/trades', coin, limit=limit)

    def getDepthInfo(self, coin: str, limit: int = 2):
        return self.bingxAPI.fetchMarketData('spot/v1/market/depth', coin, limit=limit)

    def getCandleChart(self, coin: str, interval: str = '1h', startTime: int = 0, endTime: int = 0, limit: int = 0):
        return self.bingxAPI.fetchMarketData('spot/v1/market/kline', coin, interval=interval, startTime=startTime, endTime=endTime, limit=limit)

    def getPrice(self, coin: str):
        return self.bingxAPI.fetchMarketData('spot/v1/ticker/24hr', coin)


# spotinfo = SpotInfo()
# coin = "BTC"
# currentTime = int(time.time() * 1000)
# fiveSecondAgo = currentTime - 5000
#
# print(spotinfo.getQuerySymbols(coin))
# print(spotinfo.getTranscationRecords(coin))
# print(spotinfo.getDepthInfo(coin))
# print(spotinfo.getCandleChart(coin, "4h", startTime=fiveSecondAgo, endTime=currentTime, limit=3))
# print(spotinfo.getPrice(coin))
