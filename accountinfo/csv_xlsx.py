import pandas as pd
import csv

class AssetWriter:
    def __init__(self, csv_filename='../result/asset.csv', excel_filename='../result/asset.xlsx'):
        self.csv_filename = csv_filename
        self.excel_filename = excel_filename

    def writeTotalAssetCSV(self, balances, fund_total):
        with open(self.csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["asset-currency", "balance", "free", "locked", "value-in-usdt"])
            for balance in balances:
                writer.writerow(
                    [balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                     balance['usdt_value']])
            writer.writerow(["Fund Total (USDT)", "", "", "", fund_total])
        print("Fund Total has been written to", self.csv_filename)

    def appendTotalAssetCSV(self, total_asset):
        with open(self.csv_filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["Total Asset(USDT)", "", "", "", total_asset])
        print("Total asset has been written to", self.csv_filename)
        self.csvtoExcel()
        print("CSV has been converted to", self.excel_filename)

    def csvtoExcel(self):
        df = pd.read_csv(self.csv_filename)
        df.to_excel(self.excel_filename, index=False)
