import pandas as pd
import csv

class AssetWriter:
    def __init__(self, csvFileName='result/asset.csv', excelFileName='result/asset.xlsx'):
        self.csvFileName = csvFileName
        self.excelFileName = excelFileName

    def writeTotalAssetCSV(self, balances, fundTotal):
        with open(self.csvFileName, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["asset-currency", "balance", "free", "locked", "value-in-usdt"])
            for balance in balances:
                writer.writerow(
                    [balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'],
                     balance['usdt_value']])
            writer.writerow(["Fund Total (USDT)", "", "", "", fundTotal])
        print("Fund Total has been written to", self.csvFileName)

    def appendTotalAssetCSV(self, totalAsset):
        with open(self.csvFileName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(["Total Asset(USDT)", "", "", "", totalAsset])
        print("Total asset has been written to", self.csvFileName)
        self.csvtoExcel()
        print("CSV has been converted to", self.excelFileName)

    def csvtoExcel(self):
        df = pd.read_csv(self.csvFileName)
        df.to_excel(self.excelFileName, index=False)
