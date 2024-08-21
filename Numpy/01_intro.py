import numpy as np 

a = np.array([20, 30, 40])
b = np.array([60, 70, 80])

print(a, b)
print(a+b)
print(a*b)

c = np.array([1, 2, "3"])
# Everything will be converted into string
print(c)

d = np.array([1, 2, 3.1])
# Everyting will be converted into float
print(d)