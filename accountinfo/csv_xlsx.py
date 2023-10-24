import pandas as pd
import csv

def writeFundtoCSV(balances, fund_total):
    with open('asset.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["asset-currency", "balance", "free", "locked", "value-in-usdt"])
        for balance in balances:
            writer.writerow([balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'], balance['usdt_value']])
        writer.writerow(["Fund Total (USDT)", "", "", "", fund_total])
    print("Fund Total has been written to asset.csv")


def writeTotalAssetCSV(total_asset):
    with open('asset.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Total Asset(USDT)", "", "", "", total_asset])
    print("Total asset has been written to asset.csv")
    csvToExcel('asset.csv', 'asset.xlsx')
    print("CSV has been converted to asset.csv")

def csvToExcel(csv_file, excel_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)


