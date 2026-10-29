import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

zomato = pd.DataFrame({
    "category": ["Fast Food"] * 15 + ["Desserts"] * 15,
    "order_amount": [250, 300, 280, 350, 400, 320, 290, 450, 310, 380,
                     270, 330, 420, 360, 300,
                     150, 200, 180, 220, 250, 170, 190, 300, 210, 240,
                     160, 230, 280, 200, 175]
})

sns.violinplot(data=zomato, x="category", y="order_amount")
plt.title("Order Amounts: Fast Food vs Desserts")
plt.xlabel("Restaurant Category")
plt.ylabel("Order Amount (Rs)")
plt.show()