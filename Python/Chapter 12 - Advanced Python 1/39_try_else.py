try:
    a = int(input("Hey, Enter a number: "))
    print(a)
    
except ValueError as v:
    print("Errrooorrr!")
    print(v)
    
# if try block is successfully executed then else is executed otherwise if there is an error then else will not be executed
else:
    print("I am inside else!")