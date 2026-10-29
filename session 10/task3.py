import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
steps = pd.DataFrame({
    "Day": pd.date_range("2026-10-01", periods=14),
    "Steps": np.random.randint(4000, 12000, size=14)
})

sns.set_theme(context="notebook", palette="muted")

plt.figure(figsize=(10, 5))
sns.lineplot(x="Day", y="Steps", data=steps, marker="o")
plt.title("Daily Step Counts (2 Weeks)")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()