import numpy as np

# list = [1,3,4,5]
# list2 = [2,5,6]
# # lists combine with each other but arrays add
# print(list+list2)

arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([2, 4, 6, 8])

# concatenating array
# square brackets are must
# print(np.concatenate([arr1, arr2]))

# # using axis
# arr3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# arr4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(np.concatenate([arr3, arr4], axis = 0))
# print(np.concatenate([arr3, arr4], axis = 1))

# splitting array
print(np.array_split(arr1, 2))
print(np.array_split(arr1, 3))
print(np.array_split(arr1, 4))