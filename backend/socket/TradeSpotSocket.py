from backend.market.spot import Spot
from backend.market.spotinfo import getSpotInfo
from backend.utils.utilities import PrintCommand
from backend.account.fundbalance import getFundBalance
import time

class TradeSpotSocket(Spot, PrintCommand):
    def __init__(self):
        Spot.__init__(self)
        self.spotinfo = getSpotInfo()
        self.fundbalance = getFundBalance()
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


    """
    Create a market order for buying or selling a specific coin at the current market price.
    Args:
        coin (str): The cryptocurrency for which the order will be placed.
        trade (str): Indicates whether the order is a 'BUY' or 'SELL' order.
    Returns:
        dict: Details of the created market order, including status and order ID.
    """
    def createMarketOrder(self, coin, trade):
        if trade == "BUY":
            freeUsdt = int(self.fundbalance.getCoinFree('USDT') * 100) / 100
            print(f"~ You have : {freeUsdt:.2f} USDT")
            quoteOrderQty = self.getFloatInput("Enter buying quantity: ")
            return self.toCreateOrder(coin, trade, "MARKET", quoteOrderQty=quoteOrderQty)
        else:  # SELL
            freeCoin = self.fundbalance.getCoinFree(coin)
            print(f"~ Available : {freeCoin}")
            quantity = self.getFloatInput("Enter selling quantity: ")
            return self.toCreateOrder(coin, trade, "MARKET", quantity=quantity)


    """
    Create a limit order for buying or selling a specific coin at the specific price.
    Args:
        coin (str): The cryptocurrency for which the order will be placed.
        trade (str): Indicates whether the order is a 'BUY' or 'SELL' order.
    Returns:
        dict: Details of the created market order, including status and order ID.
    """
    def createLimitOrder(self, coin, trade):
        coinPrice = self.spotinfo.getLastprice(coin)
        print(f"~ Current price : {coinPrice}")
        price = self.getFloatInput(f"Enter price to {trade.lower()}: ")
        if trade == "BUY":
            freeUsdt = int(self.fundbalance.getCoinFree('USDT')* 100) / 100
            print(f"~ You have : {freeUsdt:.2f} USDT")
            quoteOrderQty = self.getFloatInput("Enter quote order quantity: ")
            return self.toCreateOrder(coin, trade, "LIMIT", price, quoteOrderQty=quoteOrderQty)
        else:  # SELL
            freeCoin = self.fundbalance.getCoinFree(coin)
            print(f"~ Available : {freeCoin}")
            percent = self.percentage(freeCoin)
            print(f"Quantity you set: {percent}")
            #quantity = self.getFloatInput("Enter quantity: ")
            return self.toCreateOrder(coin, trade, "LIMIT", price, quantity=percent)


    """
    Interactively creates a trading order based on user input. This method guides the user
    through a series of choices to define the parameters of the order.
    Returns:
        None: The method either successfully creates an order and prints its details,
              or exits if the user inputs 'q' or an invalid option at any prompt.
    """
    def createOrder(self):
        coin = self.coinInput(self.spotinfo.getQuerySymbols)
        if coin is None:
            return  # Exit to selection page

        trade = self.getValidInput("Buy or Sell: ", ["BUY", "SELL"])
        if trade is None:
            return  # Exit to selection page

        deal = self.getValidInput("Market or Limit: ", ["MARKET", "LIMIT"])
        if deal is None:
            return  # Exit to selection page

        orderFunction = self.createMarketOrder if deal == "MARKET" else self.createLimitOrder
        order = orderFunction(coin, trade)
        if order is None:
            return  # Exit to selection page

        if order is not None and len(order) > 0:
            print(f"Order created successfully. {order}")
        else:
            print("Failed to create order. Please try again.")


    """
    Interactively cancel a trading order based on user input. This method guides the user
    through choices to define the parameters of the order.
    """
    def cancelOrder(self):
        coin = self.coinInput(self.spotinfo.getQuerySymbols)
        if coin is None:
            return

        order = self.toQueryOpenOrders(coin)
        choice = self.getValidInput(f"Select order {set(order.keys())} (q to quit): ", set(order.keys()))
        if choice is None:
            return

        cancelOrder = self.toCancelOrder(coin, order[choice]['orderId'])
        print(f"{coin} with ID: {cancelOrder[coin][0]['orderid']} order has been canceled successfully.")


    def queryOrder(self):
        coin = self.coinInput(self.spotinfo.getQuerySymbols)
        if coin is None:
            return
        orderId = str(input("Enter order id: "))
        order = self.toQueryOrder(coin, orderId)

        # print(f"Your order detail: {order}")

    def queryOpenOrders(self):
        coin = self.coinInput(self.spotinfo.getQuerySymbols)
        if coin is None:
            return
        order = self.toQueryOpenOrders(coin)

        print(f"Your open orders: {order}")

    def orderHistory(self):
        coin = self.coinInput(self.spotinfo.getQuerySymbols)
        if coin is None:
            return
        endTime = int(time.time() * 1000)  # Current time in milliseconds
        days = int(input("How many days ago: "))
        startTime = endTime - (days * 24 * 60 * 60 * 1000)  # 7 days ago in milliseconds
        order = self.getOrderHistory(coin, startTime, endTime)

        print(f"Your order history: {order}")


def getTradeSpotSocket():
    return TradeSpotSocket()


# if __name__ == "__main__":
#     user = TradeSpotSocket()
#     user.userInput()