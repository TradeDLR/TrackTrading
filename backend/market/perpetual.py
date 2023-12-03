from backend.utils.apiUtils import getBingxAPI
import time
import config
import texttable

"""
Open LONG -> side: "BUY", positionSide: "LONG"
Close LONG -> side: "SELL", positionSide: "LONG"

Open SHORT -> side: "SELL", positionSide: "SHORT"
Close SHORT -> side: "BUY", positionSide: "SHORT"
"""
class Perpetual:
    def __init__(self):
        self.bingxAPI = getBingxAPI()

    def processingData(self, data):
        processedData = {}
        coin = data['data']['symbol'].split('-')[0]
        orderInfo = {
            'orderid': data['data']['orderId'],
            'Side': data['data']['side'],
            'PositionSide': data['data']['positionSide'],
            'Quantity': data['data']['origQty'],
            'StopPrice': data['data']['stopPrice']
        }
        processedData[coin] = [orderInfo]
        # print(f"{processedData}")
        return processedData

    def openOrder(self, coin: str, type: str = "LIMIT", side: str = None, positionSide: str = None, price: float = None,
                  quantity: float = None, stopPrice: float = None, takeProfit: str = None, stopLoss: str = None):
        response = self.bingxAPI.fetchMarketData("swap/v2/trade/order", coin, method="POST", type=type, side=side,
        positionSide=positionSide, price=price, quantity=quantity, stopPrice=stopPrice, takeProfit=takeProfit, stopLoss=stopLoss)
        print(response)

    def cancelOrder(self, coin: str, orderId: int):
        orderData = self.bingxAPI.fetchMarketData("swap/v2/trade/order", coin, method="DELETE", orderId=orderId)
        processedData = self.processingData(orderData)
        print(processedData)

    def queryOrder(self, coin: str):
        response = self.bingxAPI.fetchMarketData("swap/v2/trade/order", coin, method="GET")
        print(response)

    def queryAllOrders(self, coin: str):
        response = self.bingxAPI.fetchMarketData("swap/v2/trade/openOrders", coin, method="GET")
        openOrders = response.get('data', {}).get('orders', [])
        extractedInfo = {}
        for i, order in enumerate(openOrders, start=1):
            orderInfo = {
                'OrderId': order.get('orderId'),
                'Side': order.get('side'),
                'PositionSide': order.get('positionSide'),
                'Quantity': order.get('origQty'),
                'StopPrice': order.get('stopPrice')
            }
            extractedInfo[i] = orderInfo
        if extractedInfo:
            # Create a new texttable object
            table = texttable.Texttable(max_width=0)  # Set max_width to 0 to disable wrapping
            headers = ['OrderId', 'Side', 'PositionSide', 'Quantity', 'StopPrice']

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

perpetual = Perpetual()
# perpetual.openOrder("ETH", side="SELL", positionSide="SHORT", price=2300, quantity=0.5,
#                     takeProfit="{\"type\": \"TAKE_PROFIT\", \"quantity\": 0.5,\"stopPrice\": 1200,\"price\": 1200,\"workingType\":\"MARK_PRICE\"}",
#                     stopLoss="{\"type\": \"STOP\", \"quantity\": 0.5,\"stopPrice\": 2320,\"price\": 2320,\"workingType\":\"MARK_PRICE\"}")

orderinfo = perpetual.queryAllOrders("TRB")
print(orderinfo)

# perpetual.cancelOrder("ETH")