import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

insta = pd.DataFrame({
    "likes": [120, 250, 340, 410, 520, 600, 720, 810, 950, 1100, 1250, 1400],
    "comments": [8, 15, 22, 30, 33, 45, 50, 58, 70, 74, 90, 95]
})

sns.regplot(data=insta, x="likes", y="comments")
plt.title("Instagram Likes vs Comments")
plt.xlabel("Likes")
plt.ylabel("Comments")
plt.show()