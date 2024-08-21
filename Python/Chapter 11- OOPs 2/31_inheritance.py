class Employee:
    company = "amazon"
    name = "Default"
    salary = 0
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        
class Programmer(Employee):
    language = "default"
    def showLanguage(self):
        print(f"He is good in {self.language} language")

a = Employee()
b = Programmer()

print(a.show(), b.show(), b.showLanguage())