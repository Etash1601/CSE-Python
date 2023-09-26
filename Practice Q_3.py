import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1)  Read sales2.csv file into a dataframe.
filename='/content/sales2.csv'
df-pd.read_csv(filename)
df.columns=df.columns.str.lstrip()
print(df)

#2) Display the first few records.
print(df.head(2))

#3) Describe the dataset.
print(df.describe())

#4) Check for NA values.
print(df.isnull().sum())

#5) Plot a bar graph for ord_date Vs Purchase amount.
df.plot(x = 'ord_date', y = 'purch_amt', kind = 'bar')
plt.show()

#6) Fetch the details of customer id 3001.
df[df['customer_id']==3001]

#7) Update the purchase amount of order Id 70012 as 500.
df.loc[df['ord_no' ]=-70012, 'purch_amt']=500

#8) Retrieve the order no and customer id of the maximum purchase amount.
df.loc[(df.purch_amt=max(df.purch_amt)), ['ord_no', 'customer_id', 'purch_amt']]

#9) Retrieve the order no, customer id and purchase amount whose value is greater than 1000.
df.loc[(df.purch_amt>1000), ['ord_no', 'customer_id', 'purch_ant']]

#10) Fetch the order details that are placed during the month of October.
df['ord_date']=pd.to_datetime (df['ord_date'])
df[df['ord_date'].dt.month==10]

#11) Split the dataset into groups on customer_id to summarize purch_amt with respect to each salesman id.
g=df.groupby('customer_id')
for x in g:
print(x)

gr_data = df.groupby(['customer_id', 'salesman_id']).agg({'purch_amt": "sum"})
gr_data

sum(gr_data.iloc[:,0])

#12) Calculate percentage of purch_amt in each group and rename purch_amt to purchaseAmount.
gr_data['percentage' ]-gr_data.iloc[:,0] 100/sum (gr_data.iloc[:,8]) gr_data['percentage']=round(gr_data['percentage' 1,2)
gr_data

gr_data.rename(columns('purch_amt': 'purchaseAmount'})
