a = int(input("Enter two numbers: "))
b = int(input())

if(b == 0):
    # We can raise errors
    raise ZeroDivisionError("Division with 0 is not possible!")
else:
    print(f"a/b = {a/b}")