a = int(input("Enter your age: "))

# if elif else ladder
if(a >= 18 and a<=125):
    print("You can drive!")
elif(a<=0 or a>125):
    print("You are entering an invalid age!")  
else:
    print("You cannot drive!")
    
