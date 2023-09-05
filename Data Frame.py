# Data frames

# weather.csv is a 12x6 2D data
# pd.Series(data, index, dtype, copy)
# columns are like Series_1,2,3.......Series_n


# pd.DataFrame(data, index, columns, dtype, copy)   index is for rows

import numpy as np
import pandas as pd

# create empty data frame object
df = pd.DataFrame()
print(df)

# append columns to empty data frame
df['Name'] = ['Ankit','Ankita','Yashvardhan']
df['Age'] = [19,18,20]
df['Gender'] = ['M','F','M']
print(df)

data = {'subj':["Maths","Sceince","Social Sceince","Computer Science"],'marks':[100,98,87,89],'grade':['A','A','B','A']}
df = pd.DataFrame(data)
print(df)

# reading data from csv file
filename = '/home/hadoop/Downloads/weather.csv'
df = pd.read_csv(filename)
print(df)

print(df.head(2)) # display  first two rows
print(df.sample(5)) # randomly take 5 samples

# description
print(df.shape)
print(df.dtypes)
print(df.index)
print(df.columns)

print(df['avg_high'].head(2))
print(df.describe())
print(df.describe(include="all"))
# df.columns=df.columns.str.1strips
print(df.info())
