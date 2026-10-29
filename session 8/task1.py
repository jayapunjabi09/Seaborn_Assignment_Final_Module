import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(1)
insta = pd.DataFrame({
    "followers": np.random.randint(100, 10000, 20),
    "posts": np.random.randint(10, 500, 20)
})

sns.scatterplot(data=insta, x="followers", y="posts")
plt.title("Followers vs Number of Posts")
plt.xlabel("Number of Followers")
plt.ylabel("Number of Posts")
plt.show()