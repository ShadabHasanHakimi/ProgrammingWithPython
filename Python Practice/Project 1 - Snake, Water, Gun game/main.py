'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "s", -1: "w", 0: "g"}

you = youDict[youstr]

print(f"You chose: {youstr} and computer chose: {reverseDict[computer]}")

if(computer == -1 and you == 1):
    print("You win!")
elif(computer == -1 and you == 0):
    print("You Lose!")
elif(computer == 1 and you == 0):
    print("You Win!")
elif(computer == 1 and you == -1):
    print("You Lose!")
elif(computer == 0 and you == 1):
    print("You Lose!")
elif(computer == 0 and you == -1):
    print("You Win!")
else:
    print("Draw!")