from backend.account.fundbalance import FundBalance
from backend.account.perpetualbalance import PerpetualBalance
from backend.account.standardbalance import StandardBalance
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
            ("fund balance", "fb"): self.fundBalance,
            ("perp total", "pt"): self.perpTotal,
            ("perp up", "pu"): self.perpUP,
            ("perp rp", "pr"): self.perpRP,
            ("perp balance", "pb"): self.perpFreeBalance,
            ("std total", "st"): self.stdTotal,
            ("std up", "su"): self.stdUP,
            ("std balance", "sb"): self.stdBalance
            #"quit": self.quit
        }

        descriptions = {
            "fund balance (fb)": "Get fund balance",
            "perp total/up/rp/balance (pt / pu / pr / pb)": "Get perpetual total balance/unrealized profit/realized profit/balance",
            # "perp up": "Get perpetual unrealized profit",
            # "perp rp": "Get perpetual realized profit",
            # "perp balance": "Get perpetual free balance",
            "std total/up/balance (st / su / sb)": "Get perpetual total balance/unrealized profit/balance",
            # "std up": "Get standard unrealized profit",
            # "std total": "Get standard total balance",
            "quit (Q or q)": "Quit"
        }
        PrintCommand.__init__(self, commands, descriptions, lenwave=123, lenCommand=45, lenDescipt=70)

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
        if self.updatePerpBalance():
            freeBalance = self.getPerpAsset()
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

def getSelfInfoSocket():
    return SelfInfoSocket()

# if __name__ == "__main__":
#     user = SelfInfoSocket()
#     user.userInput()
