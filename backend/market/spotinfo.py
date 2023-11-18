from backend.utils.apiUtils import getBingxAPI
import time
import datetime


class SpotInfo:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def getQuerySymbols(self, coin):
        symbols = self.bingxAPI.fetchMarketData('spot/v1/common/symbols').get('data', {}).get('symbols', [])
        symbol = coin + "-USDT"
        spot = next((s for s in symbols if s['symbol'] == symbol), None)
        return spot  # self.bingxAPI.fetchMarketData('spot/v1/common/symbols')

    # TODO:
    def getTranscationRecords(self, coin: str, limit: int = 2):
        return self.bingxAPI.fetchMarketData('spot/v1/market/trades', coin, limit=limit)#.get('data',[])

    # TODO:
    def getDepthInfo(self, coin: str, limit: int = 2):
        return self.bingxAPI.fetchMarketData('spot/v1/market/depth', coin, limit=limit)

    # TODO:
    def getCandleChart(self, coin: str, interval: str = '1h', startTime: int = int(time.time() * 1000),
                       endTime: int = int(time.time() * 1000) - 5000, limit: int = 0):
        return self.bingxAPI.fetchMarketData('spot/v1/market/kline', coin, interval=interval, startTime=startTime,
                                             endTime=endTime, limit=limit)

    def getPrice(self, coin):
        try:
            data = self.bingxAPI.fetchMarketData('spot/v1/ticker/24hr', coin)
            # print(data)
            if isinstance(coin, list):
                return {coin: info['data'][0]['lastPrice'] for coin, info in data.items()}

            elif isinstance(coin, str):
                return data['data'][0]['lastPrice']

        except (KeyError, IndexError, TypeError):
            # If the coin doesn't exist in the data or if there's any other error
            return False

def getSpotInfo():
    return SpotInfo()


# spotinfo = SpotInfo()
# coin = ["BTC", "ETH"]
# coin = "BTC"
# currentTime = int(time.time() * 1000)
# fiveSecondAgo = currentTime - 5000
#
# print(spotinfo.getQuerySymbols(coin))
# print(spotinfo.getTranscationRecords(coin))
# print(spotinfo.getDepthInfo(coin))
# print(spotinfo.getCandleChart(coin, "4h", startTime=fiveSecondAgo, endTime=currentTime, limit=3))
# print(spotinfo.getPrice(coin))