import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(1)
zomato = pd.DataFrame({
    "price": np.random.randint(100, 1000, 20),
    "delivery_time": np.random.randint(15, 60, 20)
})

sns.lmplot(data=zomato, x="price", y="delivery_time")
plt.show()