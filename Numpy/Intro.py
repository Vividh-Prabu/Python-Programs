import numpy as np

# 1-D array
arr = np.array([1, 2, 3, 4, 5])
print("1-D array:",arr)

# 2-D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[2, 4, 6]])
print("2-D array:",arr_2d)

print("Type:",type(arr))

# Shape of array [return rows and columns]
print("Shape of 1D:",arr.shape)
print("Shape of 2D:",arr_2d.shape)

# Size of the array [return total no of elements]
print("Size of 1D:",arr.size)
print("Size of 2D:",arr_2d.size)

# Dimension of the array
print("Dimension of arr:",arr.ndim)
print("Dimension of arr_2d:",arr_2d.ndim)

# Datatype of the array
print("Data type of 1D:",arr.dtype)
print("Data type of 2D:",arr_2d.dtype)

# Setting datatype explicitly
arr_2d1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]],dtype=float)
print(arr_2d1)
print("Zeros Array:\n",np.zeros((3,3))) # Making a array of given order with zeros as element(always float value)
print("Ones Array:\n",np.ones((3,3))) # Making a array of given order with ones as element(always float value)
print("Constant Array:\n",np.full((3,3),18)) # Making a array of given order with given constant values as element(datatype will be what we given)
print("Empty Array:\n",np.empty((3,3))) # Making a array with some garbage value as element


