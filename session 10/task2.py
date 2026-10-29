import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

orders = pd.DataFrame({
    "Cuisine": ["Indian"] * 40 + ["Chinese"] * 28 + ["Italian"] * 22
               + ["Mexican"] * 15 + ["Thai"] * 12
})

plt.figure(figsize=(8, 5))
sns.countplot(x="Cuisine", data=orders, palette="colorblind",
              order=orders["Cuisine"].value_counts().index)
plt.title("Food Orders by Cuisine Type")
plt.xlabel("Cuisine")
plt.ylabel("Number of Orders")
plt.show()