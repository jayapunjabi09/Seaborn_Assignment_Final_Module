import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bms = pd.DataFrame({
    "genre": ["Action", "Comedy", "Drama", "Horror", "Romance", "Action", "Comedy",
              "Drama", "Action", "Comedy", "Romance", "Horror", "Drama", "Action", "Comedy"],
    "tickets_sold": [120, 90, 75, 60, 85, 130, 95, 80, 110, 100, 70, 65, 78, 125, 88]
})

sns.countplot(data=bms, x="genre")
plt.title("Movie Genres Count")
plt.show()

sns.barplot(data=bms, x="genre", y="tickets_sold", errorbar=None) 
plt.title("Tickets Sold by Genre (No Confidence Interval)")
plt.show()