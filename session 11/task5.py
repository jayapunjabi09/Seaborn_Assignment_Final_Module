# ChatGPT Prompt:
# Generate Python code using Seaborn to create
# a heatmap and export it as a 1200 DPI SVG file.
# Adapt it to show my top 5 most-used apps.

# ChatGPT Generated Code:

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Top 5 most-used apps (example data)
apps = ["WhatsApp", "Instagram", "YouTube", "Chrome", "Spotify"]
hours = [4, 3, 2, 1.5, 1]

# Create dataframe
df = pd.DataFrame(
    [hours],
    columns=apps,
    index=["Usage Hours"]
)

# Create heatmap
sns.heatmap(
    df,
    annot=True,
    cmap="YlGnBu",
    fmt=".1f"
)

plt.title("My Top 5 Most-Used Apps")
plt.xlabel("Apps")

# Save as SVG
plt.savefig("task5_heatmap.svg", format="svg", dpi=1200, bbox_inches="tight")

plt.show()