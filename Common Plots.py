# Common Plots - Data Visualization
# Plot for Statistical Analysis

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = '/home/ex5/Downloads/plotdata.csv'
df = pd.read_csv(filename)
print(df)

df.plot(x = 'Unemployment_rate', y = 'Index_price', kind = 'scatter')
plt.show()

df.plot(x = 'Unemployment_rate', y = 'Index_price', kind = 'line')
plt.show()

df.plot(x = 'Year', y = 'Unemployment_rate', kind = 'bar')
plt.show()

df.plot(x = 'Year', y = 'Unemployment_rate', kind = 'pie')
plt.show()

# Without using pandas and just using matplotlib

x_axis = df['Year']
y_axis = df['Unemployment_rate']
plt.bar(x_axis,y_axis)
plt.title('Year vs Unemployment_rate')
plt.xlabel('Year')
plt.ylabel('Unemployment_rate')
plt.show()
# OR
x_axis = df['Year']
y_axis = df['Unemployment_rate']
plt.bar(x_axis,y_axis, color = 'red', marker='o')
plt.title('Year vs Unemployment_rate', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Unemployment_rate')
plt.grid(True)
plt.show()


my_data = [300,500,700]
my_labels = 'Tasks pending', 'Tasks Outgoing', 'Tasks Completed'
plt.pie(my_data, labels = my_labels, autopct = '%.2f%%')
plt.title('My Tasks')
plt.axis('equal')
plt.show()

# Plot Histogram

# Plot Correlation Matrix using Seaborn
# Heat Map

import seaborn as sn
import matplotlib.pyplot as plt
