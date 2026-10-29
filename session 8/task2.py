import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(2)
orders = pd.DataFrame({
    "day": range(1, 31),
    "orders": np.random.randint(50, 200, 30)
})

sns.lineplot(data=orders, x="day", y="orders", marker="o")
plt.title("Daily Zomato Food Orders (30 Days)")
plt.xlabel("Day of the Month")
plt.ylabel("Number of Orders")
plt.show()