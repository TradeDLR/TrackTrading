import ccxt
import config

from csv_xlsx import AssetWriter

class FundBalance:
    def __init__(self, exchange):
        self.exchange = exchange

    def get_coin_list_prices(self, balances):
        coin_prices = {}
        for balance in balances:
            asset = balance.get('asset', 'Unknown Asset')
            free = balance.get('free_balance', 0)
            if asset == "USDT":
                coin_prices[asset] = 1.0
            else:
                symbol = f"{asset}/USDT"
                if symbol in self.exchange.symbols:
                    ticker = self.exchange.fetch_ticker(symbol)
                    coin_prices[asset] = float(ticker['last'])
                else:
                    print(f"Warning: Symbol {symbol} not found in exchange symbols.")
        return coin_prices

    @staticmethod
    def getPrices(data, unit):
        lastPrice = data[0].get('lastPrice', 0)
        return lastPrice

    def calculation_usdt(self, balances, prices):
        total = 0
        for balance in balances:
            asset = balance['asset']
            total_balance = balance['total_balance']
            if asset in prices:
                coin_value = total_balance * prices[asset]
                total += coin_value
                balance['usdt_value'] = coin_value
            else:
                print(f"Warning: Price for {asset} not found. Setting 'usdt_value' to 0.")
                balance['usdt_value'] = 0
        return total

    @staticmethod
    def debug(balances, total_asset):
        print("asset-currency", "balance", "free", "locked", "value-in-usdt")
        for balance in balances:
            usdt_value = balance.get('usdt_value', 'N/A')  # Default to 'N/A' if 'usdt_value' is missing
            print(balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                  usdt_value)
        print("Total Asset (USDT)", "", "", "", total_asset)

    def get_fund_balance(self):
        try:
            balance = self.exchange.fetch_balance()
            balances = []
            for asset, amount in balance['total'].items():
                free_balance = balance['free'][asset]
                if free_balance != 0.0:
                    locked_balance = balance['used'][asset]
                    total_balance = free_balance + locked_balance
                    balances.append({
                        'asset': asset,
                        'free_balance': free_balance,
                        'locked_balance': locked_balance,
                        'total_balance': total_balance,
                    })

            prices = self.get_coin_list_prices(balances)
            fund_total = self.calculation_usdt(balances, prices)
            writer = AssetWriter()
            writer.writeTotalAssetCSV(balances, fund_total)
            return fund_total
        except Exception as e:
            print(f"Error occurred: {e}")
