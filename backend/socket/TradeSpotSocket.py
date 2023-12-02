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


    """
    Prompts the user to enter a cryptocurrency coin symbol (e.g., ETH, ARB) and validates 
    the input.
    Returns:
        str or None: Returns the valid coin symbol as a string if a valid input is provided. 
                     Returns None if the user enters 'q' to quit the input process.
    """
    def coinInput(self):
        while True:
            coin = str(input("Enter coin (or q to quit): ").upper())
            if coin == "Q":
                return None
            if self.spotinfo.getQuerySymbols(coin) is not None:
                return coin
            else:
                print(f"{coin} is not a valid coin. Please try again.")


    """
    Prompts the user to input a value and validates it against a set of allowed choices.
    Args:
        prompt (str): The prompt message to display to the user.
        validChoices (list of str or int): A list of valid input choices.
    Returns:
        str or int or None: The valid user input matching one of the validChoices.
                            Returns None if the user chooses to exit with 'Q'.
    """
    def getValidInput(self, prompt, validChoices):
        while True:
            userInput = input(prompt).upper()
            if userInput == "Q":
                return None

            if all(isinstance(choice, int) for choice in validChoices):
                try:
                    userInput = int(userInput)
                except ValueError:
                    pass  # Continue to the next iteration if conversion fails

            if userInput in validChoices:
                return userInput
            print(f"Invalid input. Please enter one of {validChoices}.")


    """
    Get the quantity of the coin or the price of the coin,
    and quote order quantity. 
    """
    def getFloatInput(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.upper() == "Q":
                return None  # Signal to exit
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")


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
            quoteOrderQty = self.getFloatInput("Enter buying quantity: ")
            return self.toCreateOrder(coin, trade, "MARKET", quoteOrderQty=quoteOrderQty)
        else:  # SELL
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
        price = self.getFloatInput(f"Enter price to {trade.lower()}: ")
        if trade == "BUY":
            quoteOrderQty = self.getFloatInput("Enter quote order quantity: ")
            return self.toCreateOrder(coin, trade, "LIMIT", price, quoteOrderQty=quoteOrderQty)
        else:  # SELL
            quantity = self.getFloatInput("Enter quantity: ")
            return self.toCreateOrder(coin, trade, "LIMIT", price, quantity=quantity)


    """
    Interactively creates a trading order based on user input. This method guides the user
    through a series of choices to define the parameters of the order.
    Returns:
        None: The method either successfully creates an order and prints its details,
              or exits if the user inputs 'q' or an invalid option at any prompt.
    """
    def createOrder(self):
        coin = self.coinInput()
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
        coin = self.coinInput()
        if coin is None:
            return

        order = self.toQueryOpenOrders(coin)
        choice = self.getValidInput(f"Select order {set(order.keys())} (q to quit): ", set(order.keys()))
        if choice is None:
            return

        cancelOrder = self.toCancelOrder(coin, order[choice]['orderId'])
        print(f"{coin} with ID: {cancelOrder[coin][0]['orderid']} order has been canceled successfully.")


    def queryOrder(self):
        coin = self.coinInput()
        orderId = str(input("Enter order id: "))
        order = self.toQueryOrder(coin, orderId)

        # print(f"Your order detail: {order}")

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


def getTradeSpotSocket():
    return TradeSpotSocket()


# if __name__ == "__main__":
#     user = TradeSpotSocket()
#     user.userInput()