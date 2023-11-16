from backend.trade import spot
import time

class TradeSpotSocket:
    def __init__(self):
        self.tsp = spot.Spot()

        self.commands = {
            "create": self.createOrder,
            "cancel": self.cancelOrder,
            "query": self.queryOrder,
            "open": self.queryOpenOrders,
            "history": self.orderHistory,
            "quit": self.quit
        }

        self.descriptions = {
            "create": "Create a new order",
            "cancel": "Cancel an existing order",
            "query": "Query details of an order",
            "open": "Query open orders",
            "history": "Get order history",
            "quit": "Quit"
        }

    # Define methods for each command
    def createOrder(self):
        the_coin = self.coin_input()
        trade = str(input("Buy or Sell: ").upper())

        if trade not in ["BUY", "SELL"]:
            print("Invalid input. Please enter 'buy' or 'sell'.")
            return

        deal = str(input("Market or Limit: ").upper())
        if deal not in ["MARKET", "LIMIT"]:
            print("Invalid input. Please enter 'market' or 'limit'.")
            return

        if deal == "MARKET":
            if trade == "BUY":
                quoteOrderQty = float(input("Enter quote order quantity: "))
                order = self.tsp.toCreateOrder(the_coin, trade, deal, quoteOrderQty=quoteOrderQty)
            else:  # SELL
                quantity = float(input("Enter quantity: "))
                order = self.tsp.toCreateOrder(the_coin, trade, deal, quantity=quantity)

        elif deal == "LIMIT":
            price = float(input(f"Enter price to {trade.lower()}: "))
            if trade == "BUY":
                quoteOrderQty = float(input("Enter quote order quantity: "))
                order = self.tsp.toCreateOrder(the_coin, trade, deal, price, quoteOrderQty=quoteOrderQty)
            else:  # SELL
                quantity = float(input("Enter quantity: "))
                order = self.tsp.toCreateOrder(the_coin, trade, deal, price, quantity=quantity)

        if order is not None and len(order) > 0:
            print(f"Order created successfully. {order}")
        else:
            print("Failed to create order.")

    def cancelOrder(self):
        the_coin = self.coin_input()
        orderId = str(input("Enter order id: "))
        order = self.tsp.toCancelOrder(the_coin, orderId)

        print(f"Order canceled successfully. {order}")

    def queryOrder(self, *args):
        the_coin = self.coin_input()
        orderId = str(input("Enter order id: "))
        order = self.tsp.toQueryOrder(the_coin, orderId)

        print(f"Your order detail: {order}")

    def queryOpenOrders(self, *args):
        the_coin = self.coin_input()
        order = self.tsp.toQueryOpenOrders(the_coin)

        print(f"Your open orders: {order}")

    def orderHistory(self, *args):
        the_coin = self.coin_input()
        end_time = int(time.time() * 1000)  # Current time in milliseconds
        days = int(input("How many days ago: "))
        start_time = end_time - (days * 24 * 60 * 60 * 1000)  # 7 days ago in milliseconds
        order = self.tsp.getOrderHistory(the_coin, start_time, end_time)
        
        print(f"Your order history: {order}")
    
    def quit(self):
        print("Goodbye")
        exit()

    def print_commands(self):
        print("*" * 56)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:10]) if len(command) > 15 else command.ljust(16)
            fixed_length_description = (description[:29]) if len(description) > 31 else description.ljust(32)
            print(f"* {fixedLengthCommand} -> {fixed_length_description} *")
        print("*" * 56)

    def user_input(self):
        while True:
            self.print_commands()
            user_command = input("Enter command: ").lower()
            if user_command == 'quit':
                break
            if user_command in self.commands:
                self.commands[user_command]()
            else:
                print("Unknown command. Please try again.")

    def coin_input(self):
        while True:
            crypto_coin = str(input("Enter coin: ").upper())
            if crypto_coin:
                return crypto_coin
            else:
                print("Unknown coin. Please try again.")

if __name__ == "__main__":
    user = TradeSpotSocket()
    user.user_input()