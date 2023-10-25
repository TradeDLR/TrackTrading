from FundBalance import FundBalance
from PerpetualBalance import PerpetualBalance
from StandardPosition import StandardPosition
from csv_xlsx import AssetWriter
class MainExecutor:
    @staticmethod
    def run():
        fund_balance = FundBalance()
        fund = fund_balance.get_fund_balance() or 0
        perpBalance = PerpetualBalance()
        perpAsset, perpUP, perpRP = perpBalance.get_perp_balance() or 0
        stdBalance = StandardPosition()
        # margin, stdUP = stdBalance.get_open_order() or 0
        margin, stdUP = 0, 0
        totalAsset = fund + stdUP + margin + perpAsset + perpUP + perpRP
        writer = AssetWriter()
        writer.appendTotalAssetCSV(totalAsset)

if __name__ == '__main__':
    MainExecutor.run()
