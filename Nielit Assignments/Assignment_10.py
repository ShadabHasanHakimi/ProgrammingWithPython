# Question 1
'''
Ans 1: c. Partial Argument. 

Ans 2: c. Allows immutable values only as argument. 

Ans 3: d. Allows any type of value as argument. 

Ans 4: d. Default argument allows non-default argument to follows default. 

Ans 5: c. It can return only one value. 
'''

# Question 2
'''
sum = lambda a, b, c, d: a+b+c+d
print(sum(1, 4, 5, 3))
'''

# Question 3
'''
area = lambda r: ((22/7)*r*r)
print(area(7))
'''

# Question 4
'''
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(3))
'''

# Question 5
'''
l = [4, 7, 1, 19, 3, 11]
find_max = lambda my_list: max(my_list)
print(find_max(l))
'''

# Question 6
'''
max_num = 0
def find_max(*args):
    global max_num
    for item in args:
        if item>max_num:
            max_num = item
    return max_num
print(find_max(1,6,4,8))
'''

# Question 7
'''
def find(*args):
    for item in args:
        if type(item) == int:
            if(item>=18):
                print("You are eligible to vote!")
            else:
                print("You are not eligible to vote!")

find("Shadab", 21, "Kota, Rajasthan")
'''

# Question 8
'''
total = 0
def sum(*args):
    global total
    for item in args:
        if type(item) == int:
            total += item
    return total
print(sum(10, 20, 'Ajay', 30, "#rr", 40, '50'))
'''

# Question 9
'''
count = [0, 0, 0, 0]
l = [-78, 89, 76, 12, 45, 67, 78, 91, 2, -5]
def countNum(l):
    for item in l:
        if(item<0):
            count[0] += 1
        elif(item>=0 and item<=50):
            count[1] += 1
        elif(item>50 and item<=100):
            count[2] += 1
        else:
            count[3] += 1
countNum(l)
print(f"Count for <0 : {count[0]}")
print(f"Count for 0-50 : {count[1]}")
print(f"Count for 51-100 : {count[2]}")
print(f"Count for >100 : {count[3]}")
'''
        