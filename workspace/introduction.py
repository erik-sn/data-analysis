import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

root_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(root_path, '..', 'data', 'temps.csv')

df = pd.read_csv(file_path) # df stands for "Data Frame"
df.date = pd.to_datetime(df.date)  # convert string based dates to python datetime objects

print('Looking at our data frame:')
print(df.head())  # read the top values from the data frame
print(df.describe())
print(df.dtypes)

print('Manipulating our data frame, 1985!:')
year_selection = df[(df.date >= datetime(1985, 1, 1)) & (df.date < datetime(1986, 1, 1))]
print(year_selection.head())

print('Visualizing Data')
plt.plot(df.date, df.temp, label="All Years")
plt.plot(year_selection.date, year_selection.temp, label="1985")

plt.title('Daily minimum temperatures in Melbourne, Australia')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.legend()
plt.show()
