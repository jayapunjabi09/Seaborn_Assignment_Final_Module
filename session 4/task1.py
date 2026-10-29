import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sample = pd.DataFrame({
    "product": [f"Product {i}" for i in range(1, 26)],
    "price": [499, 799, 1299, 1599, 899, 2499, 1999, 749, 1199, 999,
              1499, 3499, 649, 1799, 2199, 899, 1099, 5999, 1399, 799,
              1699, 2999, 549, 1249, 15999]
})
sample.to_csv("flipkart_prices.csv", index=False)

df = pd.read_csv("flipkart_prices.csv")

sns.boxplot(data=df, y="price")
plt.title("Flipkart Product Price Distribution")
plt.ylabel("Price (Rs)")
plt.show()