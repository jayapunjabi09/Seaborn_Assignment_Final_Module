import pandas as pd

bank_df = pd.read_csv("bank.csv", sep=";")

subscription_percentage = (
    bank_df.groupby("education")["y"]
    .apply(lambda x: (x == "yes").mean() * 100)
)

print("Subscription Percentage by Education:")
print(subscription_percentage.round(2))