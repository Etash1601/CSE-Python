# Date_Time

import numpy as np
import pandas as pd
from datetime import datetime

pd.date_range(start='2/2/2019', end='02/08/2019')
print(pd.date_range(start='2/2/2019', end='02/08/2019'))
# freq=D means day-wise
# pd.date_range(start='2/2/2019', end='02/08/2019', freq='H') Hour-wise

pd.date_range(start='2/2/2019', periods=8) # no. of days = 8

# Convert string to datetime
d = {'date': ['3/10/2000','3/11/2000','3/12/2000'], 'value': [2,3,4]}
df = pd.DataFrame(d)
print(df)
df['date'] = pd.to_datetime(df['date'])  # and  (,format="%Y-%d-%m %H:%M:%S")
print(df)

# Ignore/Coerce Errors
df['date'] = pd.to_datetime(df['date'], errors='ignore')
df
df['date'] = pd.to_datetime (df['date'], errors='coerce!)
df

# Find the age
df = pd.DataFrame({'name': ['Tom','Andy','Lucas','Pranav','Uma','Rahu','Kumar','Varun'],
                   'dob': ['08-05-1997','04-28-1996','12-16-1995','11-16-1998','06-28-1999','04-26-1997','07-09-2000','11-08-2001']})
df['dob'] = pd.to_datetime(df['dob'])
df

df['year'] = df['dob'].dt.year
df['month'] = df['dob'].dt.month
df['day'] = df['dob'].dt.day
df

# Get age from date of birth
today = pd.to_datetime('today')
df['age'] = today.year - df['dob'].dt.year
print(df)

# Setting Index
df = df.set_index(['dob'])
print(df)


# Select data with specific year and perform aggregation
df.loc['1997']
df.loc['1997','age'].sum()
df['1995'].groupby('month').sum()
df.loc['1995-12']

cond = df.index.month == 11
df[cond]  # only prints for 11th month


# Select data between two dates
df.loc['1995' : '1997']
