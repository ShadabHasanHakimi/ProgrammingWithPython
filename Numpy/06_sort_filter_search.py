import numpy as np

arr1 = np.array([2, 6, 1, 16, 3, 11, 9])
arr2 = np.array([[2, 6, 1, 16, 3, 10, 9], [40, 20, 100, 60, 30, 10, 70]])

# sort
# print(np.sort(arr1))
# print(np.sort(arr2))

# search
s = np.where(arr1 == 6)
print(s)
p = np.where(arr2 == 10)
print(p)


# filter
# true for the elements we want in the new array
# fil_arr = [True, False, True, False, True, True, False]
# new = arr1[fil_arr]
# print(new)

fil_arr = arr1>8
new=arr1[fil_arr]
print(new)