class Employee: 
    language = "Python"
    salary = 150000
    
    # dunder methods are automatically called when a new object is created
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object!")
    
    def getInfo(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Language: {self.language}")

# We can pass arguments while declaring objects if we have dunder methods
shadab = Employee("shadab_hasan", 200000, "Js")
shadab.getInfo()
