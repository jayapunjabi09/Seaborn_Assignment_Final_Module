import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.pairplot(tips, hue="sex")
plt.show()

# Observation :
# Points are colored by gender (Male and Female). Both groups overlap heavily,
# so gender does not separate the data much. Total bill and tip rise together for both.