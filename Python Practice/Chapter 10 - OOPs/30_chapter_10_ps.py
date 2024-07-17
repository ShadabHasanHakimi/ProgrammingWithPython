# Question 2
# class Calculator:
#     def add(self):
#         print("Enter two numbers to add: ")
#         Calculator.n1 = int(input())
#         Calculator.n2 = int(input())
#         print(Calculator.n1+Calculator.n2)
        
#     def mul(self):
#         print("Enter two numbers to multiply: ")
#         Calculator.n1 = int(input())
#         Calculator.n2 = int(input())
#         print(Calculator.n1*Calculator.n2)
        
#     def add(self):
#         print("Enter two numbers to subtract: ")
#         Calculator.n1 = int(input())
#         Calculator.n2 = int(input())
#         print(Calculator.n1-Calculator.n2)

# class Calculator:
#     def __init__(self, n):
#         self.n = n
#     def square(self):
#         print(f"The square of {self.n} is : {self.n*self.n}")
#     def cube(self):
#         print(f"The square of {self.n} is : {self.n*self.n*self.n}")
#     def squareroot(self):
#         print(f"The square of {self.n} is : {self.n**1/2}")
        
# calc = Calculator(4)
# calc.square()
# calc.cube()
# calc.squareroot()


# Question 5
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time!")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")
    
myTrain = Train(12399)
myTrain.book("Ranpur", "Kota")
myTrain.getStatus()
myTrain.getFare("Ranpur", "Kota")