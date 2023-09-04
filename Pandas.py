# Pandas (Series) 

import numpy as np
import pandas as pd

# creating series from array
data = np.array([10,20,30,40,50])
ser = pd.Series(data)
print(ser)

# creating series from list
l = [10,20,30,40,50]
ser = pd.Series(l)
print(ser)

# to set index for the series
sub = ["Maths","Science","STS","Language"]
marks = [100,90,80,95]
ser = pd.Series(marks, index=sub) # assigns subjects as index values
print(ser)

# create series from dictionary
sub_marks = {"Maths":100,"Science":90,"STS":80,"Language":95}
ser = pd.Series(sub_marks)
print(ser)

# series with missing values
sub = ["Maths","Science","STS","Computer"]
sub_marks = {"Maths":100,"Science":90,"STS":80,"Language":95}
ser = pd.Series(sub_marks, index=sub)
print(ser)

# extracting subjects above 90
print(ser[ser>90])

# sorting based on marks
print(ser.sort_values(ascending=False))

# ranking values
print(ser.rank(ascending=False))

# Basic Statistice
print(ser.sum())
print(ser.mean())
print(ser.median())
print(ser.std())
print(ser.max())
print(ser.idxmax())
print(ser.min())
print(ser.idxmin())
print(ser.count())
