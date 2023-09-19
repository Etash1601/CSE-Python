# Missing Data

import numpy as np
import pandas as pd
"""
df = pd.DataFrame()
df['Maths'] = [100.0,85.0,np.nan,90.0]
df['Science'] = [40.0,55.0,80.0,np.nan]
df['Social Science'] = [np.nan,50.0,70.0,98.0]
print(df)
print(df.isnull())
print(df.notnull())
print(df.isnull().sum()) # number of nan values

print(df.dropna()) # Dropping null values
print(df.fillna(0.0)) # Fill null values
df['Maths'].replace(np.nan,50,inplace=True) # replaces only math's nan value

m = round(df['Science'].mean(),2)
df['Science'].replace(np.nan,m,inplace=True) # replace with average 'm'
# OR   df['Science'].fillna(m,inplace=True)
"""
# Q
filename = '/home/hadoop/Downloads/weather_na.csv'
df1 = pd.read_csv(filename)
df2 = df1.copy()

print(df2.isnull().sum())
print(df2.dropna())

m = round(df2['record_high'].mean(),2)
df2['record_high'].fillna(m,inplace=True)
print(df2)

m = df2['avg_low'].min()
df2['avg_low'].fillna(m,inplace=True)
print(df2)

m = df2['avg_high'].max()
df2['avg_high'].fillna(m,inplace=True)
print(df2)

print("\n")
print(df1.describe())
print("\n")
print(df2.describe())
