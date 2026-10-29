import pandas as pd

bank_df = pd.read_csv("bank.csv", sep=";")

print("First 10 Rows:")
print(bank_df.head(10))

print("\nDataset Information:")
bank_df.info()