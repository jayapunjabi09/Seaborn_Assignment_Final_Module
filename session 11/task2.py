import seaborn as sns
import matplotlib.pyplot as plt

# Daily step counts
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [4000, 5500, 6000, 4500, 7000, 8000, 6500]

# Create lineplot
sns.lineplot(x=days, y=steps, marker="o")

plt.title("Daily Step Counts")
plt.xlabel("Days")
plt.ylabel("Steps")

# Save as SVG
plt.savefig("task2_steps.svg", format="svg", bbox_inches="tight")

plt.show()