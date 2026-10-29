import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

zomato = pd.DataFrame({
    "food_category": ["Pizza", "Burger", "Biryani", "South Indian"] * 5,
    "orders": [5, 8, 6, 4, 7, 9, 3, 5, 6, 7,
               4, 8, 5, 6, 3, 7, 9, 4, 5, 6]
})

sns.barplot(data=zomato, x="food_category", y="orders", estimator=sum)
plt.title("Total Number of Orders by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Total Orders")
plt.show()