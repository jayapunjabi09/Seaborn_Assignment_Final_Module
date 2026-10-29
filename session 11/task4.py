import seaborn as sns
import matplotlib.pyplot as plt

# Reusable theme function
def apply_presentation_theme():
    sns.set_theme(
        style="whitegrid",
        palette="pastel",
        font="Arial"
    )

# Apply theme
apply_presentation_theme()

# Data
categories = ["Python", "Excel", "SQL", "Power BI"]
values = [30, 25, 20, 25]

# Create pie chart
colors = sns.color_palette("pastel", 4)

plt.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    colors=colors
)

plt.title("Skills Distribution")

# Save pie chart
plt.savefig("task4_piechart.png", dpi=300, bbox_inches="tight")

plt.show()