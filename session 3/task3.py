import seaborn as sns
import matplotlib.pyplot as plt

spending = [450, 620, 800, 350, 900, 1200, 500, 750, 680, 1500,
            400, 850, 950, 600, 720, 1100, 480, 560, 890, 1300,
            640, 700, 520, 980, 1050, 430, 770, 830, 610, 920]

fig, ax = plt.subplots()
sns.histplot(spending, bins=10, stat="density", ax=ax) 
sns.kdeplot(spending, ax=ax, color="red")
ax.set_title("Monthly Spending on Zomato Orders")
ax.set_xlabel("Spending (Rs)")
ax.set_ylabel("Density")
plt.show()