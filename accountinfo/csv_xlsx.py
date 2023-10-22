import pandas as pd


def csv_to_excel(csv_file, excel_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Write the DataFrame to an Excel file
    df.to_excel(excel_file, index=False)


# Usage
csv_to_excel('accountinfo/output.csv', 'accountinfo/output.xlsx')
