import seaborn as sns
import matplotlib.pyplot as plt

days  = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
temps = [32, 34, 33, 35, 36, 37, 34]

for theme in ['darkgrid', 'whitegrid', 'ticks']:
    sns.set_theme(style=theme)           
    plt.figure()                          
    sns.lineplot(x=days, y=temps)
    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.title(f'Weekly Temperature Trend ({theme})')
    plt.savefig(f'{theme}.png')          
    plt.show()