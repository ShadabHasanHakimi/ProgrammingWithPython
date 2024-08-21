import random

n = random.randint(1, 100)
i = 1
a = int(input("Guess the number: "))
if(a == n):
    print("Congo you have guessed the correct number!")
    print(f"The number was {n}")
    print(f"You have used {i} guesses!")        
else:
        while(a!=n):        
            if(a == n):
                i+=1
                print("Congo you have guessed the correct number:")
                print(f"Your i is : {i}")
                
            elif(n>a):
                i+=1
                a = int(input("Enter a greater number:"))
            
            else:
                i+=1
                a = int(input("Enter a smaller number:"))
        else:
            print("Congo you have guessed the correct number!")
            print(f"The number was {n}")
            print(f"You have used {i} guesses!")