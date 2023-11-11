import sys
# import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.accountinfo.FundBalance import FundBalance
from backend.accountinfo.PerpetualBalance import PerpetualBalance
from backend.accountinfo.StandardBalance import StandardBalance
from backend.accountinfo.csv_xlsx import AssetWriter
from datetime import datetime

class MainExecutor:
    @staticmethod
    def run():
        fb = FundBalance()
        perp = PerpetualBalance()
        std = StandardBalance()
        fund = fb.getFundBalance() or 0
        if perp.updatePerpBalance():
            perpAsset = perp.getPerpTotal()
        else:
            perpAsset = 0
        stdAsset = std.getStdTotal() or 0

        fb.callCsvXlsx(fund)

        totalAsset = fund + perpAsset + stdAsset
        writer = AssetWriter()
        writer.appendTotalAssetCSV(totalAsset)

if __name__ == '__main__':
    start_time = datetime.now()
    MainExecutor.run()
    end_time = datetime.now()

    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")
