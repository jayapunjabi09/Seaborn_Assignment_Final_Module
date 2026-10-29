import seaborn as sns
import matplotlib.pyplot as plt

delivery_times = [25, 30, 28, 35, 40, 22, 33, 29, 31, 45,
                  27, 38, 32, 26, 34, 41, 24, 36, 30, 28,
                  39, 23, 37, 33, 29, 31, 42, 27, 35, 30,
                  26, 34, 38, 29, 32]

sns.histplot(delivery_times, bins=10)
plt.title("Distribution of Swiggy Delivery Times")
plt.xlabel("Delivery Time (minutes)")
plt.ylabel("Count")
plt.show()