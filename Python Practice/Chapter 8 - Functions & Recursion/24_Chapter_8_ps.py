# Question 1

# def findGreatest(a, b, c):
#     if(a>b and a>c):
#         print(f"{a} is the greatest!")
#     elif(b>c):
#         print(f"{b} is the greatest!")
#     else:
#         print(f"{c} is the greatest!")
        
# a = input("Enter a number: ")
# b = input("Enter a number: ")
# c = input("Enter a number: ")
# findGreatest(a, b, c)
        
        
# Question 2
# def cToF(c):
#     f = (c*(9/5))+32
#     print(f"{c}C = {f}F")

# c = int(input("Enter temperature in celcius to convert it into fahrenheit: "))
# cToF(c)


# Question 3
# print("No new line ", end="")
# print("New line")


# Question 4
# sum = 0
# def sumOfN(n):
#     if(n>0):
#         global sum 
#         sum += n
#         n-=1
#         sumOfN(n)
#     else:
#         print(f"Sum : {sum}")
# n = int(input("Enter a natural number: "))
# sumOfN(n)
        
        
# Question 4
n = int(input("Enter a number:"))
for i in range (1, n+1):
    print("*"*(n-i+1), end="")
    print("")