# Question 1
# n = int(input("Enter a number to print it's table: "))

# for i in range (1, 11):
#     print(f"{n} X {i} = {n*i}")


# Question 2
# l = ["shadab", "harry", "shaheen", "adab", "jonas"]

# for i in range (0, len(l)):
#     if(l[i].startswith("s")):
#         print(f"Hello, {l[i]}")


# Question 3
# a = int(input("Enter a number to print it's table: "))
# i = 1

# while(i!=11):
#     print(f"{a} X {i} = {a*i}")
#     i+=1


# Question 4
# a = int(input("Enter a number to print it's table: "))
# for i in range (2, a):
#     if(a%i == 0):
#         print("Not a prime number!")
#         break
# else:
#     print("It is a prime number!")


# Question 5
# n = int(input("Enter a number: "))
# sum = 0
# for i in range (1, n+1):
#     sum += i
# print(sum)

# i = 1
# while(i!=n):
#     sum+=i
#     i+=1
# print(sum)


# Question 6
# n = int(input("Enter a number to find it's factorial: "))
# fact = 1
# for i in range (2, n+1):
#     fact*=i
# print(f"Factorial of {n} = {fact}")


# Question 7
'''
  *
 ***
*****
'''
# end="" is a argument of print which don't print new line by default
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")


# Question 8
'''
*
**
***
'''
# n = int(input("Enter a number: "))
# for i in range (1, n+1):
#     for j in range (1, i+1):
#         print("*", end="")
#     print("\n", end="")


# Question 9
# n = 5
# for i in range (1, n+1):
#     if(i == 1 or i == n):
#         print("* "*(n))
#     else:
#         for j in range (1, n+1):
#             if(j == 1 or j == n):
#                 print("* ",end="")
#             else:
#                 print("  ", end="")
#         print("")
        
        
# Question 10
n = 5
for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")