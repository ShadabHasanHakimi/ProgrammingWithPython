'''
Ans 1: a. not in

Ans 2: c. >>>

Ans 3: a. 5

Ans 4: d. 20
'''

# Ans 2 and 3
'''
l = int(input("Enter the length of the Rectangle:"))
b = int(input("Enter breadth of the rectangle: "))
areaRec = l*b
perimeter = 2*(l+b)

print(f"Area of the rectangle is {areaRec} and perimeter is {perimeter}.")

r = int(input("Enter the radius of the circle"))
areaCircle = (22/7)*r*r
circumference = 2*(22/7)*r

print(f"Area of the circle is {areaCircle} and circumference is {circumference}.")
'''

# Ans 4
'''
salary = int(input("Enter your basic salary: "))
da = (salary*20)/100
ra = (salary*20)/100
grossSalary = salary+da+ra
print(f"Your gross salary is {grossSalary}.")
'''

# Ans 5
marks = 0
total = 0
for i in range(1, 6):
    marks = int(input(f"Enter marks of subject {i}"))
    total += marks
    
percentage = (total/5)

print(f"Aggregate marks obtained = {total} out of 500.")
print(f"Your percentage is {percentage}%")