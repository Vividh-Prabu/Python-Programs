import numpy as np
arr = np.array([1,2,3,4,5])
print(arr[3])

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d[2][1])

print(arr[1:3])
print(arr[::-1])
print(arr_2d[1:3:2, 1:4:2])

# Returns the boolean value based on the condition
arr_bool = arr > 2
print(arr_bool)

# Fetching the True value from the array
print(arr[arr_bool])

# Filtering based on the given condition
print(arr[arr%2==0])

# Filtering based on the condition for 2D_array
print(arr_2d[(arr_2d > 2)])
