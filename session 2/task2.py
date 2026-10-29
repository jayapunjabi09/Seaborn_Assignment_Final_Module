import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

zomato = pd.DataFrame({
    "food_category": ["Pizza", "Burger", "Biryani", "South Indian"] * 5,
    "delivery_time": [30, 25, 40, 28, 35, 22, 45, 30, 32, 27,
                      42, 26, 29, 24, 38, 31, 33, 23, 41, 29],
    "orders": np.random.randint(1, 10, 20)
})

sns.barplot(data=zomato, x="food_category", y="delivery_time", estimator=np.mean)
plt.title("Average Delivery Time by Food Category")
plt.xlabel("Food Category")
plt.ylabel("Average Delivery Time (minutes)")
plt.show()