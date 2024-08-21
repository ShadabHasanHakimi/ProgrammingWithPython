import numpy as np

# append
arr1 = np.array([20, 40, 60, 80])
# print(np.append(arr1, 90))

# for 2d
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# firstly the array will be converted into 1-d and then added
# print(np.append(arr2, 7))

# insert
# used to insert element at desired position
# print(np.insert(arr1, 2, 50))

# for 2d
# print(np.insert(arr2, 3, 7))

# using axis
# new row will be added at 1 index
# print(np.insert(arr2, 1, [50], axis=0))
# print(np.insert(arr2, 1, [50, 20, 10], axis=0))


# Delete
print(np.delete(arr1, 1))
print(np.delete(arr2, 1, axis=0))
print(np.delete(arr2, 1, axis=1))