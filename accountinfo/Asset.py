from FundBalance import FundBalance
from PerpetualBalance import PerpetualBalance
from StandardPosition import StandardPosition
from csv_xlsx import AssetWriter
class MainExecutor:
    @staticmethod
    def run():
        fund = FundBalance.getFundBalance() or 0
        perpAsset, perpUP, perpRP = PerpetualBalance.getPerpBalance() or 0
        margin, stdUP = StandardPosition.getOpenOrder() or 0

        totalAsset = fund + stdUP + margin + perpAsset + perpUP + perpRP
        writer = AssetWriter()
        writer.appendTotalAssetCSV(totalAsset)

if __name__ == '__main__':
    MainExecutor.run()
