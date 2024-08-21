'''
Ans 1: d. elif

Ans 2: d. It transfers the flow outside the body of loop

Ans 3: a. It skips the remaining body of the loop, jumps to the beginning, for current iteration. 

Ans 4: 4. str 

And 5: c. Only integer variables or messages are allowed. 
'''

# Ans 2
'''
n = int(input("Enter a number: "))
print(f"Square of entered number = {n*n}")
print(f"Cube of entered number = {n*n*n}")
'''

# Ans 3
'''
a = int(input("Enter first number: "))
b = int(input("Enter Second number: "))
if(a>b):
    print(f"{a} is greater!")
else:
    print(f"{b} is greater!")
'''

# Ans 4
'''
n = int(input("Enter a number to check whether it is odd or even: "))
if(n%2 == 0):
    print(f"{n} is even!")
else:
    print(f"{n} is odd!")
'''

# Ans 5
'''
n = int(input("Enter a number: "))
if(n%7 == 0):
    print(f"{n} is divisible by 7!")
else:
    print(f"{n} is not divisible by 7!")
'''

# Ans 6
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a>b and a>c):
    print(f"{a} is greater!")
elif(b>c):
    print(f"{b} is greater!")
else:
    print(f"{c} is greater!")
'''

# Ans 7
'''
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''

# Ans 8
'''
a = int(input("Enter a three digit number: "))
b = a
c = 0
i = 100
while(b!=0):
    c += (b%10)*i
    b = int(b/10)
    i = int(i/10)

if(c==a):
    print("Given number is palindrome!")
else:
    print("Given number is not palindrome!")
'''

# Ans 9
'''
cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

if(cp == sp):
    print("0 profit, 0 loss!")
elif(cp>sp):
    print(f"Loss of {cp-sp} rupees!")
else:
    print(f"Profit of {sp-cp} rupees!")
'''

# Ans 10
p = int(input("Enter physics marks: "))
c = int(input("Enter chemistry marks: "))
m = int(input("Enter maths marks: "))

total = p+c+m
avg = total/3

if(avg >= 80):
    print(f"Average marks: {avg}, and Grade: Distinction")
elif(avg >= 60 and avg < 80):
    print(f"Average marks: {avg}, and Grade: First Division")
elif(avg >= 45 and avg < 60):
    print(f"Average marks: {avg}, and Grade: Second Division")
elif(avg >= 40 and avg < 45):
    print(f" Average marks: {avg}, and Grade: Pass")
else:
    print(f"Promotion not granted, and Average marks: {avg}")
    
