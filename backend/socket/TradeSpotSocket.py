from backend.market.spot import Spot
from backend.market.spotinfo import getSpotInfo
from backend.utils.utilities import PrintCommand
import time

class TradeSpotSocket(Spot, PrintCommand):
    def __init__(self):
        Spot.__init__(self)
        self.spotinfo = getSpotInfo()
        commands = {
            ("create", "cr"): self.createOrder,
            ("cancel", "ca"): self.cancelOrder,
            ("query", "qu"): self.queryOrder,
            ("open", "o"): self.queryOpenOrders,
            ("history", "h"): self.orderHistory
            #"quit": self.quit
        }

        descriptions = {
            "create (cr)": "Create a new order",
            "cancel (ca)": "Cancel an existing order",
            "query (qu)": "Query details of an order",
            "open (o)": "Query open orders",
            "history (h)": "Get order history",
            "quit (Q or q)": "Quit"
        }

        PrintCommand.__init__(self, commands, descriptions)

    def createOrder(self):
        coin = self.coinInput()
        while True:
            trade = str(input("Buy or Sell: ").upper())
            if trade in ["BUY", "SELL"]:
                while True:
                    deal = str(input("Market or Limit: ").upper())
                    if deal in ["MARKET", "LIMIT"]:
                        break
                    else:
                        print("Invalid input. Please enter 'market' or 'limit'.")

                if deal == "MARKET":
                    if trade == "BUY":
                        quoteOrderQty = float(input("Enter quote order quantity: "))
                        order = self.toCreateOrder(coin, trade, deal, quoteOrderQty=quoteOrderQty)
                    else:  # SELL
                        quantity = float(input("Enter quantity: "))
                        order = self.toCreateOrder(coin, trade, deal, quantity=quantity)

                elif deal == "LIMIT":
                    while True:
                        try:
                            price = float(input(f"Enter price to {trade.lower()}: "))
                            break
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")

                    if trade == "BUY":
                        quoteOrderQty = float(input("Enter quote order quantity: "))
                        order = self.toCreateOrder(coin, trade, deal, price, quoteOrderQty=quoteOrderQty)
                    else:  # SELL
                        quantity = float(input("Enter quantity: "))
                        order = self.toCreateOrder(coin, trade, deal, price, quantity=quantity)

                if order is not None and len(order) > 0:
                    data = self.process_order_data(order)
                    print(f"Order created successfully. {data}")
                    break  # Exit the loop after successful order creation
                else:
                    print("Failed to create order. Please try again.")
            else:
                print("Invalid input. Please enter 'buy' or 'sell'.")

    def cancelOrder(self):
        coin = self.coinInput()
        orderId = str(input("Enter order id: "))
        order = self.toCancelOrder(coin, orderId)

        print(f"Order canceled successfully. {order}")

    def queryOrder(self):
        coin = self.coinInput()
        orderId = str(input("Enter order id: "))
        order = self.toQueryOrder(coin, orderId)

        print(f"Your order detail: {order}")

    def queryOpenOrders(self):
        coin = self.coinInput()
        order = self.toQueryOpenOrders(coin)

        print(f"Your open orders: {order}")

    def orderHistory(self):
        coin = self.coinInput()
        endTime = int(time.time() * 1000)  # Current time in milliseconds
        days = int(input("How many days ago: "))
        startTime = endTime - (days * 24 * 60 * 60 * 1000)  # 7 days ago in milliseconds
        order = self.getOrderHistory(coin, startTime, endTime)

        print(f"Your order history: {order}")

    def coinInput(self):
        while True:
            coin = str(input("Enter coin: ").upper())
            if coin:
                if self.spotinfo.getQuerySymbols(coin) is not None:
                    return coin
                else:
                    print(f"{coin} is not a valid coin. Please try again.")
            else:
                print("Unknown coin. Please try again.")

    def process_order_data(self,order_data):
        processed_data = {}
        coin = order_data['data']['symbol'].split('-')[0]

        # Extract the relevant information from the order data
        order_info = {
            'orderid': order_data['data']['orderId'],
            'price': order_data['data']['price'],
            'origQty': order_data['data']['origQty'],
            'status': order_data['data']['status'],
            'side': order_data['data']['side']
        }
        processed_data[coin] = [order_info]
        #print(f"{processed_data}")
        return processed_data

def getTradeSpotSocket():
    return TradeSpotSocket()


# if __name__ == "__main__":
#     user = TradeSpotSocket()
#     user.userInput()