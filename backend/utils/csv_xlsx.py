import pandas as pd
import csv
import os

class AssetWriter:
    def __init__(self, csvFileName='result/asset.csv', excelFileName='result/asset.xlsx'):
        self.csvFileName = csvFileName
        self.excelFileName = excelFileName

    def writeAndUpdateAsset(self, balances, fundTotal, totalAsset=None):
        os.makedirs(os.path.dirname(self.csvFileName), exist_ok=True)

        # Writing the initial data to CSV
        with open(self.csvFileName, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["asset-currency", "balance", "free", "locked", "value-in-usdt"])
            for balance in balances:
                writer.writerow(
                    [balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                     balance['usdt_value']])
            writer.writerow(["Fund Total (USDT)", "", "", "", fundTotal])

            # Appending total asset if provided
            if totalAsset is not None:
                writer.writerow(["Total Asset(USDT)", "", "", "", totalAsset])

        print("Asset information has been written to", self.csvFileName)

        # Converting CSV to Excel
        self.csvtoExcel()
        print("CSV has been converted to", self.excelFileName)

    def csvtoExcel(self):
        df = pd.read_csv(self.csvFileName)
        df.to_excel(self.excelFileName, index=False)

def writer():
    return AssetWriter()
