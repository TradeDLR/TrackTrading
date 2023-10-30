import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from accountinfo.FundBalance import FundBalance
from accountinfo.PerpetualBalance import PerpetualBalance
from accountinfo.StandardBalance import StandardBalance

class SelfInfoSocket:
    def __init__(self):
        self.fund = FundBalance()
        self.perp = PerpetualBalance()
        self.std = StandardBalance()

        self.commands = {
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

        self.descriptions = {
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

    def fundBalance(self):
        fund_total = self.fund.getFundBalance()  # Directly call the getFundBalance method
        if fund_total is not None:
            print(f"Total Fund Balance: {fund_total} USDT")
        else:
            print("Failed to fetch fund balance.")

    def perpTotal(self):
        if self.perp.updatePerpBalance():
            total = self.perp.getPerpTotal()
            print(f"Perpetual Total Balance: {total} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def perpUP(self):
        if self.perp.updatePerpBalance():
            unrealized_profit = self.perp.getPerpUP()
            print(f"Perpetual Unrealized Profit: {unrealized_profit} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def perpRP(self):
        if self.perp.updatePerpBalance():
            realized_profit = self.perp.getPerpRP()
            print(f"Perpetual Realized Profit: {realized_profit} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def perpFreeBalance(self):
        if self.perp.updatePerpBalance():
            free_balance = self.perp.getPerpAsset()
            print(f"Perpetual Free Balance: {free_balance} USDT")
        else:
            print("Failed to fetch perpetual balance.")

    def stdBalance(self):
        balance = self.std.getStdBalance()
        print(f"Standard Balance: {balance} USDT")

    def stdUP(self):
        unrealized_profit = self.std.getStdUP()
        print(f"Standard Unrealized Profit: {unrealized_profit} USDT")

    def stdTotal(self):
        total = self.std.getStdTotal()
        print(f"Standard Total Balance: {total} USDT")

    # def mkinfo(self):
    #     print(f"Latest Price of {}")

    def quit(self):
        print("Goodbye")
        exit()

    # def ()

    def print_commands(self):
        print("*" * 103)
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixedLengthCommand = (command[:24]) if len(command) > 24 else command.ljust(25)
            fixed_length_description = (description[:65]) if len(description) > 69 else description.ljust(70)
            print(f"* {fixedLengthCommand} -> {fixed_length_description} *")
        print("*" * 103)

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

if __name__ == "__main__":
    user = SelfInfoSocket()
    user.user_input()
