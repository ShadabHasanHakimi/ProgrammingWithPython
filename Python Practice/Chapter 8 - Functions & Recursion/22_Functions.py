# funciton definition
def avg():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    c = int(input("Enter number:"))
    avg = (a+b+c)/3
    print(avg)

# function call
# avg()

# There are two types of functions in python: Built-in and user defined functions
# For eg len() is a built in function and avg() is a user defined function

# Function with arguments
def hello(name):
    print(f"Hello! {name}.") 
    return "successful"

# name = input("Enter your name:")
# hello(name)

# return value in function
print(hello("shadab"))