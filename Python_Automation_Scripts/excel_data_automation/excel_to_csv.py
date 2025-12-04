import pandas as pd

def excel_to_csv(excel_file, csv_file):
    df = pd.read_excel(excel_file)
    df.to_csv(csv_file, index=False)
    print("Converted Excel to CSV!")

# Example
excel_to_csv("data.xlsx", "data.csv")
