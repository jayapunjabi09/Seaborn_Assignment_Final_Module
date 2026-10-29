import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(5)
price = np.random.randint(500, 5000, 30)
flipkart = pd.DataFrame({
    "price": price,
    "reviews": (price * 0.4 + np.random.normal(0, 400, 30)).clip(10).round(0)
})

g = sns.lmplot(
    data=flipkart, x="price", y="reviews",
    scatter_kws={"color": "green"}
)
g.set_axis_labels("Product Price (Rs)", "Number of Reviews")
g.figure.suptitle("Flipkart Price vs Number of Reviews", y=1.02)
plt.show()