import numpy as np

# arr = np.array([1,2,3,4,5,6])
# print("Original Array:",arr)
#
# #reshape = arr.reshape(2,3)
# reshape = np.reshape(arr,(3,2))
# print("Reshaped Array:\n",reshape)
# reshape[0][0] = 18
# print("Original Array:\n",arr)
# print("Reshaped Array:\n",reshape)

# arr = np.array([[1,2,3],[4,5,6]])
# print("Original array:",arr)
#
# # Ravel changes the 2D or 3D array to 1D array and reflect if any changes done
# ravel = arr.ravel()
# print("Ravel array:",ravel)
# ravel[0] = 18
# print("Original array:",arr)
# print("Ravel array:",ravel)
#
# # Flatten also changes the 2D or 3D array to 1D array and will not changes the original array
# flatten = arr.flatten()
# print("Flatten:",flatten)
# flatten[0] = 200
# print("Original array:\n",arr)

arr = np.array([1,2,3,4,5])
arr1 = np.array([6,7,8,9,10])
print("Original array:",arr)

# It will stack both array horizontally
print(np.hstack([arr,arr1]))

# It will stack both the array vertically
print(np.vstack([arr,arr1]))

# It will join both the array in both horizontally and vertically
print(np.concatenate([arr,arr1]))

arr2 = np.array([[1,2],[3,4]])
# Will swap the 1 with 3 and 2 with 4
print(arr2.T)
