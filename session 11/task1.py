import seaborn as sns
import matplotlib.pyplot as plt

# Food categories and orders
food = ["Pizza", "Burger", "Biryani", "Momos", "Ice Cream"]
orders = [120, 90, 150, 80, 110]

# Create barplot
sns.barplot(x=food, y=orders, color="skyblue")

plt.title("Orders per Food Category")
plt.xlabel("Food Category")
plt.ylabel("Number of Orders")

# Save chart
plt.savefig("task1_barplot.png", dpi=300, bbox_inches="tight")

plt.show()