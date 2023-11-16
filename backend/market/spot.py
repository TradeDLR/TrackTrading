from backend.utils.apiUtils import BingxAPI
import config
import time

class Spot:
    APIURL = "https://open-api.bingx.com"
    APIKEY = config.API_KEY
    SECRETKEY = config.SECRET_KEY

    def __init__(self):
        self.bingxAPI = BingxAPI()

    def spots(self, req: str, coin: str, method: str = None, **kwargs):
        path = '/openApi/spot/' + req
        paramsMap = {"symbol": coin + "-USDT"}
        paramsMap.update({k: v for k, v in kwargs.items() if v is not None})
        paramsStr = self.bingxAPI.parseParams(paramsMap)
        payload = {}
        return self.bingxAPI.sendRequest(method, path, paramsStr, payload)

    def toCreateOrder(self, coin: str, side: str = None, type: str = None, price: float = None, quantity: float = None, quoteOrderQty: float = None):
        return self.spots("v1/trade/order", coin, method="POST", type=type, side=side, price=price, quantity=quantity, quoteOrderQty=quoteOrderQty)

    def toCancelOrder(self, coin: str, orderId: str):
        return self.spots("v1/trade/cancel", coin, method="POST", orderId=orderId)

    def toQueryOrder(self, coin: str, orderId: str):
        return self.spots("v1/trade/query", coin, method="GET", orderId=orderId)

    def toQueryOpenOrders(self, coin: str):
        return self.spots("v1/trade/openOrders", coin, method="GET")

    def getOrderHistory(self, coin: str, pageIndex: int = None, startTime:int = None, endTime:int = None, pageSize: int = None):
        return self.spots("v1/trade/historyOrders", coin, method="GET", startTime=startTime, endTime=endTime, pageIndex=1, pageSize=5)

# Example usage
if __name__ == '__main__':
    spot_instance = Spot()
    # Create an order
    #response = spot_instance.toCreateOrder(coin="BTC", type="LIMIT", side="BUY", price=20000, quoteOrderQty=10)
    #print("placeOrder:", response)

    # Cancel an order
    cancel_response = spot_instance.toCancelOrder(coin="BTC", orderId="1725015097778012160")
    print("cancelOrder:", cancel_response)

    # Query an order
    #query_response = spot_instance.queryOrder(coin="BTC", orderId="1724603042994487296")
    #print("queryOrder:", query_response)

    # Query open orders
    open_orders_response = spot_instance.toQueryOpenOrders(coin="BTC")
    print("queryOpenOrders:", open_orders_response)


    end_time = int(time.time() * 1000)  # Current time in milliseconds
    start_time = end_time - (7 * 24 * 60 * 60 * 1000)  # 7 days ago in milliseconds

    # Query order history
    #order_history_response = spot_instance.orderHistory(coin="ETH", startTime=start_time, endTime=end_time, pageIndex=1, pageSize=99)
    #print("orderHistory:", order_history_response)
