import numpy as np

l = [10,20,30,40,15,18]
arr = np.array(l)
print(arr)

# creating a rank 1 array
arr = np.array([1,2,3])
print("Array with rank 1: \n",arr)
# creating a rank 2 array
arr = np.array([[1,2,3],[4,5,6]])
print("Array with rank 2: \n",arr)

print("\nArray is of type: ",type(arr))
print("Dimension: ",arr.ndim)
print("Shape: ",arr.shape)
print("Size: ",arr.size)
print("Data type: ",arr.dtype)


# Creating Arrays
arr = np.arange(0,101,5)
print(arr)

# linespace(start, stop, num=50(no. of samples)
arr = np.arange(0,101,5)
print(arr)

# Reshaping array (original size of the array remains the same)
# 3x4 to 2x2x3

arr = np.array([[1,2,3,4],
              [5,2,4,2],
              [1,2,0,1]])
newarr = arr.reshape(2,2,3)
print(arr)
print("\n")
print(newarr)
