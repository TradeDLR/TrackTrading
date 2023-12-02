from backend.utils.apiUtils import getBingxAPI
import time
import config

class Futures:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def futures(self, req: str, coin: str, type: str = None, side: str = None, positionSide: str = None, price: int = None, quantity: int = None, stopPrice: int = None):
        payload = {}
        path = '/openApi/swap/' + req
        method = "POST"
        paramsMap = {"symbol": coin + "-USDT",
                     "type": type,
                     "side": side,
                     "positionSide": positionSide,
                     "price": price,
                     "quantity": quantity,
                     "stopPrice": stopPrice}
        paramsMap = {k: v for k, v in paramsMap.items() if v is not None}
        paramsStr = self.bingxAPI.parseParams(paramsMap)
        return self.bingxAPI.sendRequest(method, path, paramsStr, payload)
    
    def placeOrder(self, coin: str, type: str = None, side: str = None, positionSide: str = None, price: int = None, quantity: int = None):
        return self.futures("v2/trade/order", coin, side=side, positionSide=positionSide, type=type, price=price, quantity=quantity)
    
    def setOrder(self, coin: str, type: str = None, side: str = None, positionSide: str = None, price: int = None, quantity: int = None, stopPrice: int = None):
        return self.futures("v2/trade/order", coin, side=side, positionSide=positionSide, type=type, price=price, quantity=quantity, stopPrice=stopPrice)

    def setPosition(self, coin: str, type: str = None, side: str = None, positionSide: str = None, price: int = None, quantity: int = None, stopPrice: int = None):
        return self.futures("v2/trade/order", coin, side=side, positionSide=positionSide, type=type, price=price, quantity=quantity, stopPrice=stopPrice)
