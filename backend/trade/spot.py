from accountinfo.apiUtils import BingxAPI
import time
import config

class Spot:
    APIURL = "https://open-api.bingx.com"
    APIKEY = config.API_KEY
    SECRETKEY = config.SECRET_KEY

    def __init__(self):
        self.bingxAPI = BingxAPI()

    def spots(self, req: str, coin: str, type: str = None, side: str = None, positionSide: str = None, price: int = None, quantity: int = None, stopPrice: int = None):
        payload = {}
        path = '/openApi/swap/' + req
        method = "POST"
        paramsMap = {"symbol": coin + "-USDT",
                     "side": side,
                     "type": type,
                     "timeInForce": timeInForce,
                     "quantity": quantity,
                     "quoteOrderQty": quoteOrderQty,
                     "price": price,
                     "recvWindow": recvWindow}
        paramsMap = {k: v for k, v in paramsMap.items() if v is not None}
        paramsStr = self.bingxAPI.parseParams(paramsMap)
        return self.bingxAPI.sendRequest(method, path, paramsStr, payload)
    
    def placeOrder(self, coin: str, type: str = None, side: str = None, positionSide: str = None, price: int = None, quantity: int = None):
        return self.futures("v2/trade/order", coin, side=side, positionSide=positionSide, type=type, price=price, quantity=quantity)
    


if __name__ == '__main__':
    print("demo:", demo())
