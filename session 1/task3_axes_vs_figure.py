import seaborn as sns
import matplotlib.pyplot as plt

days  = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temps = [32, 34, 33, 35, 36, 37, 34]

sns.lineplot(x=days, y=temps)
plt.xlabel('Days')
plt.ylabel('Temperature (°C)')
plt.title('Weekly Temperature Trend')
plt.show()

# Figure-level: creates its own whole figure
sns.relplot(x=days, y=temps, kind='line')
plt.title('Weekly Temperature Trend')
plt.show()
