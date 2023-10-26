import ccxt
import config
from FundBalance import FundBalance
from PerpetualBalance import PerpetualBalance
from StandardBalance import StandardBalance

exchange = ccxt.bingx({
            'apiKey': config.API_KEY,
            'secret': config.SECRET_KEY,
        })

class UserSocket:
    def __init__(self, exchange):
        self.exchange = exchange

        self.perp = PerpetualBalance(self.exchange)
        self.std = StandardBalance(self.exchange)
        self.fund = FundBalance(self.exchange)

        self.commands = {
            "fund balance": self.fundBalance,
            "perp total": self.perpTotal,
            "perp up": self.perpUP,
            "perp rp": self.perpRP,
            "perp free balance": self.perpFreeBalance,
            "std total": self.stdTotal,
            "std up": self.stdUP,
            "std rp": self.stdRP,
            "std free balance": self.stdFreeBalance,
            "done": self.quit
        }

        self.descriptions = {
            "fund balance": "get fund balance",
            "perp total": "get perpetual total asset",
            "perp up": "get perpetual unrealized profit",
            "perp rp": "get perpetual realized profit",
            "perp free balance": "get perpetual free balance",
            "std total": "get std total asset",
            "std up": "get std unrealized profit",
            "std rp": "get std realized profit",
            "std free balance": "get std free balance",
            "done": "Quit"
        }

    def fundBalance(self):
        return self.fund.getFundBalance()

    def perpTotal(self):
        return self.perp.getPerpTotal()

    def perpUP(self):
        return self.perp.getPerpUP()

    def perpRP(self):
        return self.perp.getPerpRP()

    def perpFreeBalance(self):
        return self.perp.getPerpBalance()

    def stdTotal(self):
        return self.std.getStdTotal()

    def stdUP(self):
        return self.std.getStdUP()

    def stdRP(self):
        return self.std.getStdRP()

    def stdFreeBalance(self):
        return self.std.getStdBalance()

    def quit(self):
        print("GoodBYE")
        exit()

    def print_commands(self):
        print("*" * 54)
        print("* Enter" + " " * 46 + "*")
        for command, description in self.descriptions.items():
            # Truncate the command if it is too long and adjust the spacing
            fixed_length_command = (command[:20] + '...') if len(command) > 23 else command.ljust(23)
            fixed_length_description = (description[:20] + '...') if len(description) > 23 else description.ljust(23)
            print(f"* {fixed_length_command} -> {fixed_length_description} *")
        print("*" * 54)

    def user_input(self):
        while True:
            self.print_commands()
            user_command = input("Enter command: ").lower()
            if user_command == 'done':
                break
            if user_command in self.commands:
                self.commands[user_command]()
            else:
                print("Unknown command. Please try again.")

if __name__ == "__main__":
    user = UserSocket(exchange)
    user.user_input()
