import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(4)
n = 30
hours = np.random.uniform(0, 8, n).round(1)
method = ["self-study"] * 15 + ["coaching"] * 15
scores = np.where(
    np.array(method) == "coaching",
    85 - hours * 3 + np.random.normal(0, 5, n),
    80 - hours * 6 + np.random.normal(0, 5, n)
).clip(0, 100).round(0)

students = pd.DataFrame({
    "youtube_hours": hours,
    "exam_score": scores,
    "preparation_method": method
})

sns.lmplot(data=students, x="youtube_hours", y="exam_score", col="preparation_method")
plt.show()