import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales = pd.DataFrame({
    "Category": ["Electronics", "Fashion", "Home & Kitchen", "Books", "Beauty"],
    "Sales": [120000, 95000, 70000, 40000, 55000]
})

# Custom corporate theme
sns.set_theme(
    style="whitegrid",         
    palette="deep",             
    context="talk",             
    font_scale=1.2,             
    rc={
        "grid.linestyle": "--",
        "grid.alpha": 0.6,
        "axes.edgecolor": "#2874F0", 
        "axes.titleweight": "bold"
    }
)

plt.figure(figsize=(10, 6))
sns.barplot(x="Category", y="Sales", data=sales)
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()