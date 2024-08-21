# Class: A class is a blueprint for creating objects, here Employee is a class
class Employee:
    language = "py"
    salary = 150000
    # We can also define a function in a class
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")
        
    # if there is no need of object in a method than we can declare it static
    @staticmethod
    def greet():
        print("good morning!")
 
# Object: an object is a instance of class, here shadab is an object
shadab = Employee()
shadab.name = "Shadab Hasan Hakimi"
print(shadab.name, shadab.language, shadab.salary)
# Here name is object/instance attribute and salary and language are class attributes as they directly belong to the class

# instance attributes takes preference over class attributes
shadab.language = "js"
# language will be changed
print(shadab.language)

# calling function inside the class
shadab.greet()
# shadab.getInfo()
Employee.getInfo(shadab)