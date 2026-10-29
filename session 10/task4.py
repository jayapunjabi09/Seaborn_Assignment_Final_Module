import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"] * 2,
    "Group": ["G1"] * 4 + ["G2"] * 4,
    "Value": [23, 45, 12, 36, 30, 28, 19, 41]
})

sns.set_theme(context="talk", palette="deep")
plt.figure(figsize=(9, 5))
sns.barplot(x="Category", y="Value", hue="Group", data=data)
plt.title("Before: deep + talk")
plt.show()

sns.set_theme(context="poster", palette="colorblind")
plt.figure(figsize=(11, 6))
sns.barplot(x="Category", y="Value", hue="Group", data=data)
plt.title("After: colorblind + poster")
plt.tight_layout()
plt.show()

# Differences observed:
# 1. Colors: 'colorblind' is less saturated and easier to tell apart
#    for people with color vision deficiency.
# 2. Size: 'poster' makes titles, labels, ticks, legend and lines
#    noticeably larger than 'talk'.
# 3. The larger elements take more space, so the layout needs
#    more room (larger figsize / tight_layout).