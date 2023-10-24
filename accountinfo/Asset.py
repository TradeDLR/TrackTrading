from FundBalance import FundBalance
from PerpetualBalance import PerpetualBalance
from StandardPosition import StandardPosition
from csv_xlsx import writeTotalAssetCSV

class MainExecutor:
    @staticmethod
    def run():
        fund = FundBalance.getFundBalance()
        perpAsset, perpUP, perpRP = PerpetualBalance.getPerpBalance()
        margin, stdUP = StandardPosition.getOpenOrder()

        totalAsset = fund + stdUP + margin + perpAsset + perpUP + perpRP
        writeTotalAssetCSV(totalAsset)

if __name__ == '__main__':
    MainExecutor.run()
