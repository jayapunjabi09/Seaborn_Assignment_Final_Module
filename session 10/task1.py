import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Songs_Streamed": [42, 38, 55, 47, 63, 80, 72]
})

sns.set_theme(context="notebook")
plt.figure(figsize=(8, 5))
sns.barplot(x="Day", y="Songs_Streamed", data=data)
plt.title("Songs Streamed per Day (Default Context)")
plt.show()

sns.set_theme(context="poster")
plt.figure(figsize=(10, 6))
sns.barplot(x="Day", y="Songs_Streamed", data=data)
plt.title("Songs Streamed per Day (Poster Context)")
plt.tight_layout()
plt.show()

# Observation: 
# In 'poster' the fonts, tick labels, bar edges and lines
# Are scaled up, so the plot is bigger and bolder than the default.