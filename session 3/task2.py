import seaborn as sns
import matplotlib.pyplot as plt

steps = [6500, 8200, 7100, 9500, 10200, 4300, 5600, 7800, 8900, 11000,
         6200, 7400, 9100, 8000, 5200, 4800, 7600, 9800, 10500, 8300,
         6900, 7200, 9000, 11500, 5900, 6400, 8700, 9300, 7000, 8100]

sns.kdeplot(steps, fill=True)
plt.title("Distribution of Daily Step Counts (30 Days)")
plt.xlabel("Steps per Day")
plt.ylabel("Density")
plt.show()