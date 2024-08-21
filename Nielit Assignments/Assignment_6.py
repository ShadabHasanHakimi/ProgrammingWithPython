# Ans 1
'''
Ans 1: d. elif 

Ans 2: d. It transfers the flow outside the body of loop. 

Ans 3: a. It skips the remaining body of the loop, jumps to the beginning. 

Ans 4: d. string 

Ans 5: d. Data type of sequence is 'RANGE'. 
'''

# Ans 2
'''
m = int(input("Enter start value: "))
n = int(input("Enter end value: "))

sum_odd = 0
sum_even = 0

for i in range(m, n+1):
    if (i%2 == 0):
        sum_even+=i
    else:
        sum_odd+=i

print(f"Sum of odd numbers from {m} to {n} is: {sum_odd}")
print(f"Sum of even numbers from {m} to {n} is: {sum_even}")
'''

# Ans 3
'''
n = int(input("Enter a number: "))
for i in range (1, 11):
    print(f"{n} X {i} = {n*i}")
'''

# Ans 4
'''
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
'''

# Ans 5
'''
n = int(input("Enter a number: "))
fact = 1
for i in range (2, n+1):
    fact *= i
print(f"Factorial of {n} is {fact}")
'''

# Ans 6
'''
s = input("Enter a string to count vowels in it: ")
vowelCount = 0
for i in range(0, len(s)):
    if("a" == s[i] or "e" == s[i] or "i" == s[i] or "o" == s[i] or "u" == s[i]):
        vowelCount += 1
    elif("A" == s[i] or "E" == s[i] or "I" == s[i] or "O" == s[i] or "U" == s[i]):
        vowelCount += 1
print(f"Vowels in {s} = {vowelCount}")        
'''

# Ans 7
'''
X = [10, 20, 30, 40, 50]
total = 0
for item in X:
    total += item
avg = total/len(X)
print(avg)
'''

# Ans 8
'''
a.
for i in range(1, 21, 2):
    print(i)

b.
for i in range(4, 44, 4):
    print(i)

c.
n = 1
print(n)
for i in range(1, 10):
    n += 2*i+1
    print(n)

e. 
for i in range(-5, -55, -5):
    print(i) 

f.
for i in range(-20, 0, 2):
    print(i)
'''

# Ans 9
'''
Month = [ "Jan", "Feb", "Mar", "Apr" , "May", "Jun" ]
for i in range(0, len(Month)+1):
    if(i%2 != 0):
        print(Month[i])
'''

# Ans 10
'''
n = 0
sum = 0
for i in range(1, 20, 2):
    if(n%2 == 0):
        sum += i
    n += 1
print(sum)
'''