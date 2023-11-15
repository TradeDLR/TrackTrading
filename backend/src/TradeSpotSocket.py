from backend.trade import spot

class TradeSpotSocket:
    def __init__(self):
        self.trasp = spot.Spot()

        self.commands = {
            "create order": self.createOrder,
            "cancel order": self.cancelOrder,
            "query order": self.queryOrder,
            "query open orders": self.queryOpenOrders,
            "order history": self.orderHistory,
            "quit": self.quit
        }

        self.descriptions = {
            "create order": "Create a new order",
            "cancel order": "Cancel an existing order",
            "query order": "Query details of an order",
            "query open orders": "Query open orders",
            "order history": "Get order history",
            "quit": "Quit"
        }

    # Define methods for each command
    def createOrder(self, *args):
        # Implementation for creating an order
        pass

    def cancelOrder(self, *args):
        # Implementation for canceling an order
        pass

    def queryOrder(self, *args):
        # Implementation for querying an order
        pass

    def queryOpenOrders(self, *args):
        # Implementation for querying open orders
        pass

    def orderHistory(self, *args):
        # Implementation for getting order history
        pass

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