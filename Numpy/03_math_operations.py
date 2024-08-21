import numpy as np

arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([2, 4, 6, 8])

# addition
# print(arr1+arr2)
# print(np.add(arr1, arr2))

# for multi-d arrays
arr3 = np.array([[1, 3, 5, 7], [1, 2, 3, 4]])
arr4 = np.array([[2, 4, 6, 8], [5, 6, 7, 8]])

# print(arr3+arr4)

# subtraction
# print(arr1-arr2)
# print(np.subtract(arr3, arr4))

# multiplication
# print(arr1*arr2)
# print(np.multiply(arr3, arr4))

# exponentiation
pow = 3
print(np.power(arr1, pow))

# square root
print(np.sqrt(arr4))