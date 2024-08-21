import numpy as np

# Creating a matrix using numpy 
# arr = np.array([[10, 20, 30, 40], [20, 40, 60, 80], [10, 30, 50, 70]])
# print(arr)


# Slicing: all the elements except last index
# arr = np.array([1, 2, 3, 4, 5])
# print(arr[0:3])
# print(arr[:4])
# print(arr[3:])

# for multi dimensional arrays
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print(arr[0:2, 0:2])
# # elements will be equal
# print(arr[0:2, 0:3])
# print(arr[0:2, 2:4])

# # second element of second row
# print(arr[1, 1])
# print(arr[1, 1:3])

# returns number of rows, number of columns
# print(np.shape(arr))
# returns number of elements
# print(np.size(arr))
# returns number of dimensions
# print(np.dim(arr))

print(arr.dtype)
# converting type of elements
print(arr.astype(float))