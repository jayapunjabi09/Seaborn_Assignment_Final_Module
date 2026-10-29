import seaborn as sns
import matplotlib.pyplot as plt

runs = [165, 180, 142, 195, 210, 158, 172, 188, 134, 205,
        176, 160, 148, 190, 225, 170, 155, 183, 199, 168,
        145, 178, 162, 215, 150, 186, 173, 192, 140, 168]

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, b in zip(axes, [5, 10, 20]):
    sns.histplot(runs, bins=b, ax=ax)
    ax.set_title(f"bins={b}")
    ax.set_xlabel("Runs")
plt.tight_layout()
plt.show()

# With bins=5 the plot is very smooth and hides detail, so you only see the overall shape.
# With bins=10 the shape is clear, with most scores between 150 and 190.
# With bins=20 the bars get thin and uneven, showing noise and small gaps in the data.