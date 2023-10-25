from FundBalance import FundBalance
from PerpetualBalance import PerpetualBalance
from StandardBalance import StandardBalance
from csv_xlsx import AssetWriter
import ccxt
import config
from datetime import datetime

class MainExecutor:
    @staticmethod
    def run():
        exchange = ccxt.bingx({
            'apiKey': config.API_KEY,
            'secret': config.SECRET_KEY,
        })
        fund_balance = FundBalance(exchange)
        fund = fund_balance.get_fund_balance() or 0
        perpBalance = PerpetualBalance(exchange)
        perpAsset, perpUP, perpRP = perpBalance.get_perp_balance() or 0
        stdBalance = StandardBalance(exchange)
        margin, stdUP, stdRP = stdBalance.get_std_balance() or 0
        totalAsset = fund + margin + stdUP + stdRP + perpAsset + perpUP + perpRP
        writer = AssetWriter()
        writer.appendTotalAssetCSV(totalAsset)

if __name__ == '__main__':
    start_time = datetime.now()
    MainExecutor.run()
    end_time = datetime.now()

    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")