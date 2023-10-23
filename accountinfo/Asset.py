import sys
sys.path.append('../TrackTrading')  # Replace with the absolute path to your TrackTrading directory
from FundBalance import get_fund_balance
from FutureBalance import get_opened_order
from csv_xlsx import write_total_asset_to_csv

if __name__ == '__main__':
    fund = get_fund_balance()
    margin, unrealized_profit = get_opened_order()

    # Not finished yet, need to add the asset in future account.
    future_asset = 0
    total_asset = fund + unrealized_profit + margin + future_asset
    write_total_asset_to_csv(total_asset)
    print(total_asset)
