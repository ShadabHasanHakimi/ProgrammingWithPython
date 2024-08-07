# for finding log
import math

class Student:
    def __init__(self, first_name, last_name, gender, year, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.year = year
        self.gpa = gpa
    
    def show_student(self):
        print(f"First Name : {self.first_name}")
        print(f"Last Name : {self.last_name}")
        print(f"Gender : {self.gender}")
        print(f"Year : {self.year}")
        print(f"GPA : {self.gpa}")
    
    def student_study_time(self, study_time):
        if(self.gpa >= 4.0):
            return
        self.gpa += math.log(study_time)
        if(self.gpa > 4.0):
            self.gpa = 4.0
            

s1 = Student("Shadab", "Hasan Hakimi", "male", "final-year", 1.19)
s2 = Student("Josh", "Hazlewood", "male", "first-year", 2.28)
s3 = Student("Lagartha", "Lothbrok", "female", "first-year", 2.92)
s4 = Student("Joe", "Biden", "male", "second-year", 3.29)
s5 = Student("Riya", "Maheshwari", "female", "third-year", 1.88)

student_GPA = [s1, s2, s3, s4, s5]

# Before updation
for student in student_GPA:
    student.show_student()
    print("***********************")
    
student_GPA[0].student_study_time(30)
student_GPA[1].student_study_time(60)
student_GPA[2].student_study_time(90)
student_GPA[3].student_study_time(120)
student_GPA[4].student_study_time(180)

# After updation
for student in student_GPA:
    student.show_student()
    print("***********************")