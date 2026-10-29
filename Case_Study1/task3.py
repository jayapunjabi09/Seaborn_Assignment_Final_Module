import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bank_df = pd.read_csv("bank.csv", sep=";")

sns.boxplot(
    data=bank_df,
    x="y",
    y="age",
    order=["no", "yes"]
)

plt.title("Age vs Term Deposit Subscription")
plt.xlabel("Subscribed")
plt.ylabel("Age")

plt.tight_layout()
plt.show()