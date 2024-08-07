class Employee:
    # def __init__(self):
    def __init__(self, *args):
        if(len(args)<4):
            self.id = 1000
            self.firstName = "Unknown"
            self.lastName = "Unknown"
            self.salary = 0
        else:
            self.id = args[0]
            self.firstName = args[1]
            self.lastName = args[2]
            self.salary = args[3]      
    def display(self):
        print(f"Employee id: {self.id} \n First Name: {self.firstName} \n Last Name: {self.lastName} \n Salary: {self.salary}")

emp1 = Employee()
emp2 = Employee(1001, "Shadab", "Hasan Hakimi", 50000)
emp1.display()
emp2.display()