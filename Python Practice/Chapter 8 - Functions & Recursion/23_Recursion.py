# When a function calls itself then this is known as recursion.

n = int(input("Enter a number to find its factorial:"))

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
    
print(factorial(n))