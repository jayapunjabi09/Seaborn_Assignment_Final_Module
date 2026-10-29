import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bank_df = pd.read_csv("bank.csv", sep=";")

print(bank_df["y"].value_counts())

sns.countplot(
    data=bank_df,
    x="y",
    order=["no", "yes"]
)

plt.title("Term Deposit Subscription")
plt.xlabel("Subscribed")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.show()