class Student:
    def __init__(self,stu_name,stu_age):
        self.name=stu_name
        self.age=stu_age
    def display(self):
        print(f"{self.name} is {self.age} years old")

stu1=Student('Sunanda',24)
stu1.display()
        