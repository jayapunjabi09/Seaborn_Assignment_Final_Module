import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(4)
hours = np.random.uniform(0, 8, 25).round(1)
scores = (90 - hours * 6 + np.random.normal(0, 6, 25)).clip(0, 100).round(0)

students = pd.DataFrame({"youtube_hours": hours, "exam_score": scores})

sns.regplot(data=students, x="youtube_hours", y="exam_score")
plt.title("YouTube Hours vs Exam Scores")
plt.xlabel("Hours Spent on YouTube")
plt.ylabel("Exam Score")
plt.show()

print("Correlation:", round(students["youtube_hours"].corr(students["exam_score"]), 2))

# Interpretation :
# The regression line slopes downward, so the trend is negative.
# Students who spend more hours on YouTube tend to have lower exam scores.