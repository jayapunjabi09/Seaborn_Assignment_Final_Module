import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(3)
songs = np.random.randint(5, 100, 40)
playlist = pd.DataFrame({
    "num_songs": songs,
    "duration_min": (songs * 3.5 + np.random.normal(0, 20, 40)).round(0)
})

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

sns.regplot(data=playlist, x="num_songs", y="duration_min", ax=axes[0])
axes[0].set_title("Linear Fit")

sns.regplot(data=playlist, x="num_songs", y="duration_min", lowess=True, ax=axes[1])
axes[1].set_title("Lowess Smoothing")

plt.tight_layout()
plt.show()