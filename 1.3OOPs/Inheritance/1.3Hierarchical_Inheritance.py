class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Child class 1
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def display_student(self):
        self.display_person()
        print(f"Grade: {self.grade}")

# Child class 2
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        self.display_person()
        print(f"Subject: {self.subject}")

# Child class 3
class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_staff(self):
        self.display_person()
        print(f"Department: {self.department}")

# Create objects
s = Student("Alice", 16, "10th Grade")
t = Teacher("Mr. John", 40, "Mathematics")
st = Staff("Mrs. Smith", 35, "Library")

# Call their methods
print("---- Student Info ----")
s.display_student()

print("\n---- Teacher Info ----")
t.display_teacher()

print("\n---- Staff Info ----")
st.display_staff()

print(Staff.mro())
