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
        s1 = datetime.now()
        fundBalance = FundBalance(exchange)
        fund = fundBalance.getFundBalance() or 0
        fundBalance.callCsvXlsx(fund)
        e1 = datetime.now()
        el1 = e1 - s1
        print(f"fundBalance Time taken: {el1} seconds")

        s2 = datetime.now()
        perp = PerpetualBalance(exchange)
        perpTotal = perp.getPerpTotal() or 0
        e2 = datetime.now()
        el2 = e2 - s2
        print(f"perpBalance Time taken: {el2} seconds")

        s3 = datetime.now()
        stdBalance = StandardBalance(exchange)
        stdTotal = stdBalance.getStdTotal() or 0
        e3 = datetime.now()
        el3 = e3 - s3
        print(f"stdBalance Time taken: {el3} seconds")

        totalAsset = fund + stdTotal + perpTotal
        writer = AssetWriter()
        writer.appendTotalAssetCSV(totalAsset)

if __name__ == '__main__':
    startTime = datetime.now()
    MainExecutor.run()
    endTime = datetime.now()

    elapsedTime = endTime - startTime
    print(f"Time taken: {elapsedTime} seconds")