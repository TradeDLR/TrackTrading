from backend.account.FundBalance import FundBalance
from backend.account.PerpetualBalance import PerpetualBalance
from backend.account.StandardBalance import StandardBalance
from backend.utils.utilities import PrintCommand
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class SelfInfoSocket(FundBalance, PerpetualBalance, StandardBalance, PrintCommand):
    def __init__(self):
        FundBalance.__init__(self)
        PerpetualBalance.__init__(self)
        StandardBalance.__init__(self)

        commands = {
            "fund balance": self.fundBalance,
            "perp total": self.perpTotal,
            "perp up": self.perpUP,
            "perp rp": self.perpRP,
            "perp balance": self.perpFreeBalance,
            "std total": self.stdTotal,
            "std up": self.stdUP,
            "std balance": self.stdBalance,
            "quit": self.quit
        }

        descriptions = {
            "fund balance": "Get fund balance",
            "perp total/up/rp/balance": "Get perpetual total balance/unrealized profit/realized profit/balance",
            # "perp up": "Get perpetual unrealized profit",
            # "perp rp": "Get perpetual realized profit",
            # "perp balance": "Get perpetual free balance",
            "std total/up/balance": "Get perpetual total balance/unrealized profit/balance",
            # "std up": "Get standard unrealized profit",
            # "std total": "Get standard total balance",
            "quit": "Quit"
        }
        PrintCommand.__init__(self, commands, descriptions)

    def fundBalance(self):
        fundTotal = self.getFundBalance()  # Directly call the getFundBalance method
        if fundTotal is not None:
            print(f"Total Fund Balance: {fundTotal} USDT")
        else:
            print("Failed to fetch fund balance.")

    def perpTotal(self):
        if self.updatePerpBalance():
            total = self.getPerpTotal()
            print(f"Perpetual Total Balance: {total} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def perpUP(self):
        if self.updatePerpBalance():
            unrealizedProfit = self.getPerpUP()
            print(f"Perpetual Unrealized Profit: {unrealizedProfit} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def perpRP(self):
        if self.updatePerpBalance():
            realizedProfit = self.getPerpRP()
            print(f"Perpetual Realized Profit: {realizedProfit} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def perpFreeBalance(self):
        if self.perp.updatePerpBalance():
            freeBalance = self.perp.getPerpAsset()
            print(f"Perpetual Free Balance: {freeBalance} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def stdBalance(self):
        balance = self.getStdBalance()
        print(f"Standard Balance: {balance} USDT")

    def stdUP(self):
        unrealizedProfit = self.getStdUP()
        print(f"Standard Unrealized Profit: {unrealizedProfit} USDT")

    def stdTotal(self):
        total = self.getStdTotal()
        print(f"Standard Total Balance: {total} USDT")

    # def mkinfo(self):
    #     print(f"Latest Price of {}")


    def printCommands(self):
        print("*" * 103)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:24]) if len(command) > 24 else command.ljust(25)
            fixedLengthDescription = (description[:65]) if len(description) > 69 else description.ljust(70)
            print(f"* {fixedLengthCommand} -> {fixedLengthDescription} *")
        print("*" * 103)

    def userInput(self):
        while True:
            self.printCommands()
            userCommand = input("Enter command: ").lower()
            if userCommand == 'quit':
                break
            if userCommand in self.commands:
                self.commands[userCommand]()
            else:
                print("Unknown command. Please try again.")

def getSelfInfoSocket():
    return SelfInfoSocket()

# if __name__ == "__main__":
#     user = SelfInfoSocket()
#     user.userInput()
