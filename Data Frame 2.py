# Append and drop
import numpy as np
import pandas as pd

df1 = pd.DataFrame([[1,2],[3,4]], columns  = ['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]], columns  = ['a','b'])
df1 = df1.append(df2)
print(df1)
print("After deleting:")
df1 = df1.drop(0)
print(df1)

# to add a row
# df1.loc[len(df1.index)] = [7,7]
                   
# Q1)
data = {'Name':["Ankit","Ankita","Yashv","Vikal"],'Cat_1 marks':[15,22,24,21],'Cat_2 marks':[18,24,21,23],'Fat marks':[45,50,37,49]}
df = pd.DataFrame(data)
print(df)
# adding one row
df.loc[len(df.index)] = ["Pavan",23,23,41]
# adding one column
df['Total'] = df['Cat_1 marks'] + df['Cat_2 marks'] + df['Fat marks']
print(df)
# sort by total marks
print(df.sort_values('Total'))


# Q2)
filename = '/home/ex5/Downloads/weather.csv'
df = pd.read_csv(filename)
print(df)

# sort rows based one column name
print(df.sort_values(by='record_high',ascending=True))

# Slicing rows
print(df[2:4])

print(df[['month','record_high']])


# Filtering
print(df[df["month"]=="Feb"])

print(df[df["month"].isin(['Feb','Jun','Dec'])])

# Create a new column
df['avg_day'] = (df.avg_low + df.avg_high)/2
print(df.head())

df['new col'] = [0,0,0,0,1,1,1,1,2,2,2,2]
print(df.head())

# Writing to csv file
filename1 = '/home/ex5/Downloads/weather1.csv'
df.to_csv(filename1)
