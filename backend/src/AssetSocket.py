import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from backend.account.fundbalance import FundBalance
from backend.account.perpetualbalance import PerpetualBalance
from backend.account.standardbalance import StandardBalance
from backend.utils.csv_xlsx import AssetWriter


class AssetSocket(FundBalance, PerpetualBalance, StandardBalance, AssetWriter):
    def __init__(self):
        # Initialize parent classes
        FundBalance.__init__(self)
        PerpetualBalance.__init__(self)
        StandardBalance.__init__(self)
        AssetWriter.__init__(self)

    def run(self):
        fund = self.getFundBalance() or 0
        if self.updatePerpBalance():
            perpAsset = self.getPerpTotal()
        else:
            perpAsset = 0
        stdAsset = self.getStdTotal() or 0

        # self.callCsvXlsx(fund)

        totalAsset = fund + perpAsset + stdAsset
        self.writeAndUpdateAsset(self.balances, totalAsset)


def getAssetSocket():
    return AssetSocket()

# if __name__ == '__main__':
#     start_time = datetime.now()
#     AssetSocket().run()
#     end_time = datetime.now()
#     elapsed_time = end_time - start_time
#     print(f"Time taken: {elapsed_time} seconds")
