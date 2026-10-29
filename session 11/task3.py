import seaborn as sns
import matplotlib.pyplot as plt

# Apply darkgrid style
sns.set_style("darkgrid")

# Data
subjects = ["Python", "Excel", "SQL", "Power BI"]
marks = [85, 90, 80, 95]

# Create chart
sns.barplot(
    x=subjects,
    y=marks,
    hue=subjects,
    palette="viridis",
    legend=False
)

plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

# Save high-resolution PNG
plt.savefig("task3_darkgrid.png", dpi=1200, bbox_inches="tight")

plt.show()