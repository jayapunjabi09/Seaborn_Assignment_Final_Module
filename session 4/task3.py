import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

ticket_prices = np.array([1200, 1500, 1800, 2000, 2200, 2500, 1700, 1900, 2100,
                          1600, 2300, 2400, 1800, 2000, 2200, 9000, 12000, 1500])

sns.boxplot(x=ticket_prices)
plt.title("IPL Match Ticket Prices")
plt.xlabel("Ticket Price (Rs)")
plt.show()

q1 = np.percentile(ticket_prices, 25)
q3 = np.percentile(ticket_prices, 75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
outliers = ticket_prices[(ticket_prices < lower) | (ticket_prices > upper)]

print("Lower whisker limit:", lower)
print("Upper whisker limit:", upper)
print("Outliers:", outliers)