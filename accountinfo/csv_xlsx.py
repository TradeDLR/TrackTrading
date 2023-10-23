import pandas as pd
import csv

def write_fund_to_csv(balances, fund_total):
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["asset-currency", "balance", "free", "locked", "value-in-usdt"])
        for balance in balances:
            writer.writerow([balance['asset'], balance['total_balance'], balance['free_balance'], balance['locked_balance'], balance['usdt_value']])
        writer.writerow(["Fund Total (USDT)", "", "", "", fund_total])


def write_total_asset_to_csv(total_asset):
    with open('output.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["Total Asset(USDT)", "", "", "", total_asset])
    csv_to_excel('output.csv', 'output.xlsx')

def csv_to_excel(csv_file, excel_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)


