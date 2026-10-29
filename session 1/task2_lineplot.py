import seaborn as sns           
import matplotlib.pyplot as plt 

print(sns.__version__)           
print(plt.matplotlib.__version__) 

days  = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temps = [32, 34, 33, 35, 36, 37, 34]

sns.lineplot(x=days, y=temps)    
plt.xlabel('Days')              
plt.ylabel('Temperature (°C)')   
plt.title('Weekly Temperature Trend')
plt.show()                      