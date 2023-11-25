from backend.utils.apiUtils import getBingxAPI
import time

class SpotInfo:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def getQuerySymbols(self, coin):
        return self.bingxAPI.fetchMarketData('spot/v1/common/symbols', coin)

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

    def getLastprice(self, coin):
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



spotinfo = SpotInfo()

#coin = ["BTC", "ETH"]
#coin = "BTC"
#currentTime = int(time.time() * 1000)
#fiveSecondAgo = currentTime - 5000000

#print(spotinfo.getQuerySymbols(coin))
#print(spotinfo.getTransactionRecords(coin, 1))
#print(spotinfo.getDepthInfo(coin, 2))
#print(spotinfo.getCandleChart(coin, "1m", limit=2))
#print(spotinfo.getPrice(coin))
