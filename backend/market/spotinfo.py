from backend.utils.apiUtils import getBingxAPI
import time

class SpotInfo:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def getQuerySymbols(self, coin):
        response = self.bingxAPI.fetchMarketData('spot/v1/common/symbols', coin)
        #print(f"{response}")
        data = response.get('data', {})
        if data['symbols'] == None:
            return None
        else:
            symbols = data['symbols'][0]
            return symbols

    def getTransactionRecords(self, coin: str, limit: int = 0):
        response =  self.bingxAPI.fetchMarketData('spot/v1/market/trades', coin, limit=limit)
        #print(f"{response}")
        info = response['data']
        data = []
        for n in range(limit):
            data.append(info[n])
        return data

    def getDepthInfo(self, coin: str, limit: int = 0):
        response = self.bingxAPI.fetchMarketData('spot/v1/market/depth', coin, method="GET",  limit=limit)
        #print(f"{response}")
        info = response['data']
        results = {'bid_price': [], 'bid_qty': [], 'ask_price': [], 'ask_qty': []}
        for n in range(limit):
            results['bid_price'].append(info['bids'][n][0])
            results['bid_qty'].append(info['bids'][n][1])
            results['ask_price'].append(info['asks'][n][0])
            results['ask_qty'].append(info['asks'][n][1])
        return results

    def getCandleChart(self, coin: str, interval: str, startTime: int = 0, endTime: int = 0, limit: int = 0):
        response = self.bingxAPI.fetchMarketData('spot/v2/market/kline', coin, interval=interval, limit=limit)
        #print(f"{response}")
        info = response['data']
        list = {'open_price': [], 'max_price': [], 'min_price': [], 'close_price': []}
        for n in range(limit):
            list['open_price'].append(info[n][1])
            list['max_price'].append(info[n][2])
            list['min_price'].append(info[n][3])
            list['close_price'].append(info[n][4])
        #return results
        fields = ["open_price", "max_price", "min_price", "close_price"]
        results = tuple(list.get(field, '') for field in fields)
        return results

    def getPrice(self, coin):
        response = self.bingxAPI.fetchMarketData('spot/v1/ticker/24hr', coin)
        #print(f"{response}")
        info = response['data'][0]
        fields = ["openPrice", "highPrice", "lowPrice", "lastPrice", "volume"]
        results = tuple(info.get(field, '') for field in fields)

        return results


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

coin = "BTC"

#currentTime = int(time.time() * 1000)
#fiveSecondAgo = currentTime - 5000000

#print(spotinfo.getQuerySymbols(coin))
#print(spotinfo.getTransactionRecords(coin, 2))
#print(spotinfo.getDepthInfo(coin, 2))
print(spotinfo.getCandleChart(coin, "1m", limit=2))
#print(spotinfo.getPrice(coin))
