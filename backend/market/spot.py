from backend.utils.apiUtils import getBingxAPI
import config
import time
import texttable

class Spot:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def processingData(self, data):
        processedData = {}
        coin = data['data']['symbol'].split('-')[0]
        orderInfo = {
            'orderid': data['data']['orderId'],
            'price': data['data']['price'],
            'origQty': data['data']['origQty'],
            'status': data['data']['status'],
            'side': data['data']['side']
        }
        processedData[coin] = [orderInfo]
        # print(f"{processedData}")
        return processedData

    def toCreateOrder(self, coin: str, side: str = None, type: str = None, price: float = None, quantity: float = None, quoteOrderQty: float = None):
        orderData = self.bingxAPI.fetchMarketData("spot/v1/trade/order", coin, method="POST", type=type, side=side, price=price, quantity=quantity, quoteOrderQty=quoteOrderQty)
        processedData = self.processingData(orderData)
        return processedData

    def toCancelOrder(self, coin: str, orderId: str):
        orderData = self.bingxAPI.fetchMarketData("spot/v1/trade/cancel", coin, method="POST", orderId=orderId)
        processedData = self.processingData(orderData)
        return processedData

    def toQueryOrder(self, coin: str, orderId: str):
        return self.bingxAPI.fetchMarketData("spot/v1/trade/query", coin, method="GET", orderId=orderId)

    def toQueryOpenOrders(self, coin: str):
        response = self.bingxAPI.fetchMarketData("spot/v1/trade/openOrders", coin, method="GET")
        openOrders = response.get('data', {}).get('orders', [])
        extractedInfo = {}
        for i, order in enumerate(openOrders, start=1):
            orderInfo = {
                'orderId': order.get('orderId'),
                'price': order.get('price'),
                f'{coin} Quantity': order.get('origQty'),
                'side': order.get('side'),
                'USDT Quantity': order.get('origQuoteOrderQty')
            }
            extractedInfo[i] = orderInfo

        if extractedInfo:
            # Create a new texttable object
            table = texttable.Texttable(max_width=0)  # Set max_width to 0 to disable wrapping
            headers = ['price', f'{coin} Quantity', 'side', 'USDT Quantity']

            # Add headers
            table.header([''] + list(extractedInfo.keys()))

            # Add rows for each field
            for field in headers:
                row = [field] + [order[field] for order in extractedInfo.values()]
                table.add_row(row)

            # Draw the table
            print(table.draw())
        else:
            print("No open orders available.")

        return extractedInfo

    def getOrderHistory(self, coin: str, pageIndex: int = None, startTime:int = None, endTime:int = None, pageSize: int = None):
        return self.bingxAPI.fetchMarketData("spot/v1/trade/historyOrders", coin, method="GET", startTime=startTime, endTime=endTime, pageIndex=1, pageSize=5)

# Example usage
if __name__ == '__main__':
    spot_instance = Spot()
    # Create an order
    #response = spot_instance.toCreateOrder(coin="BTC", type="LIMIT", side="BUY", price=20000, quoteOrderQty=10)
    #print("placeOrder:", response)

    # Cancel an order
    # cancel_response = spot_instance.toCancelOrder(coin="ARB", orderId="1725015097778012160")
    # print("cancelOrder:", cancel_response)

    # Query an order
    #query_response = spot_instance.queryOrder(coin="BTC", orderId="1724603042994487296")
    #print("queryOrder:", query_response)

    # Query open orders
    # open_orders_response = spot_instance.toQueryOpenOrders(coin="ARB")
    # print("queryOpenOrders:", open_orders_response)


    # end_time = int(time.time() * 1000)  # Current time in milliseconds
    # start_time = end_time - (7 * 24 * 60 * 60 * 1000)  # 7 days ago in milliseconds

    # Query order history
    #order_history_response = spot_instance.getOrderHistory(coin="ADA", startTime=start_time, endTime=end_time, pageIndex=1, pageSize=99)
    #print("orderHistory:", order_history_response)
