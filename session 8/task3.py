import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.DataFrame({
    "movie": [f"Movie {i}" for i in range(1, 16)],
    "rating": [8.1, 7.5, 6.8, 8.9, 7.2, 6.5, 7.9, 8.4, 6.9, 7.7, 8.0, 7.1, 6.6, 8.6, 7.4],
    "reviews": [1200, 800, 450, 2000, 650, 400, 1100, 1700, 500, 900, 1300, 600, 380, 1850, 750],
    "genre": ["Action", "Comedy", "Drama", "Action", "Comedy", "Drama", "Action", "Drama",
              "Comedy", "Action", "Drama", "Comedy", "Comedy", "Action", "Drama"]
})

sns.relplot(data=movies, x="rating", y="reviews", hue="genre", kind="scatter")
plt.show()