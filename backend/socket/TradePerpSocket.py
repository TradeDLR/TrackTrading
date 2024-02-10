from backend.market.perpetual import Perpetual
from backend.market.perpinfo import getPerpInfo
from backend.utils.utilities import PrintCommand
# from backend.socket.SelfInfoSocket import getSelfInfoSocket
from backend.account.perpetualbalance import getPerpBalance
import time

class TradePerpSocket(Perpetual, PrintCommand):
    def __init__(self):
        Perpetual.__init__(self)
        self.perpinfo = getPerpInfo()
        self.perpbalance = getPerpBalance()
        commands = {
            ("create", "cr"): self.createPerpOrder,
            ("cancel", "ca"): self.cancelOrder,
            ("query", "qu"): self.queryOrder,
            ("queryall", "qa"): self.queryAllOrders,
            # "quit": self.quit
        }

        descriptions = {
            "create (cr)": "Create a new order",
            "cancel (ca)": "Cancel an existing order",
            "query (qu)": "Query details of an order",
            "query all (qa)": "Query all opened orders",
            "quit (Q or q)": "Quit"
        }

        PrintCommand.__init__(self, commands, descriptions)

    def marketOrder(self, coin, trade, positionSide):
        pass

    def limitOrder(self, coin, trade, positionSide):
        price = self.getFloatInput(f"Enter price to {trade.lower()}: ")
        if trade == "BUY":
            quantity = self.getFloatInput("Enter quote order quantity: ")
            return self.openOrder(coin, trade, "LIMIT", price, quantity=quantity)
        else:  # SELL
            quantity = self.getFloatInput("Enter quote order quantity: ")
            return self.openOrder(coin, trade, "LIMIT", price, quantity=quantity)

    def createPerpOrder(self):
        if self.perpbalance.updatePerpBalance():
            freeBalance = self.perpbalance.getPerpAsset()
            print(f"Perpetual Free Balance: {freeBalance} USDT")
        else:
            print("Failed to fetch perpetual balance.")
        coin = self.coinInput(self.perpinfo.getContractInfo)
        if coin is None:
            return
        trade = self.getValidInput("Enter trade (BUY or SELL): ", ["BUY", "SELL"])
        if trade is None:
            return

        positionSide = self.getValidInput("Enter position side (LONG or SHORT): ", ["LONG", "SHORT"])
        if positionSide is None:
            return

        type = self.getValidInput("Enter order type (LIMIT or MARKET): ", ["LIMIT", "MARKET"])
        if type is None:
            return

        orderFunction = self.marketOrder if type == "MARKET" else self.limitOrder
        order = orderFunction(coin, trade, positionSide)
        if order is None:
            print("Failed to create order.")
            return
        if order.get("status") == "FILLED":
            print(f"Order {order.get('orderId')} has been filled.")
        else:
            print(f"Order {order.get('orderId')} has been created.")


        # if trade == "BUY":
        #     quantity = self.getFloatInput("Enter quantity: ")
        #     stopPrice = self.getFloatInput("Enter stop price: ")
        #     takeProfit = self.getFloatInput("Enter take profit: ")
        #     stopLoss = self.getFloatInput("Enter stop loss: ")
        #     return self.openOrder(coin, type, trade, positionSide, price, quantity, stopPrice, takeProfit, stopLoss)
        # else:  # SELL
        #     quantity = self.getFloatInput("Enter quantity: ")
        #     stopPrice = self.getFloatInput("Enter stop price: ")
        #     takeProfit = self.getFloatInput("Enter take profit: ")
        #     stopLoss = self.getFloatInput("Enter stop loss: ")
        #     return self.openOrder(coin, type, trade, positionSide, price, quantity, stopPrice, takeProfit, stopLoss)
        #


def getTradePerpSocket():
    return TradePerpSocket()