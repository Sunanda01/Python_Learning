class University:
    def __init__(self,uni_name,**kwargs):
        self.uni_name=uni_name
        super().__init__(**kwargs)
    def showDetails(self):
        print(f"UNIVERSITY NAME=> {self.uni_name}")
        
class Course(University):
    def __init__(self,c_name,**kwargs):
        self.c_name=c_name
        super().__init__(**kwargs)
    def showDetails(self):
        super().showDetails()
        print(f"COURSE NAME=> {self.c_name}")
    
class Branch(University):
    def __init__(self, b_name,**kwargs):
        self.b_name=b_name
        super().__init__(**kwargs)
    def showDetails(self):
        super().showDetails()
        print(f"BRANCH NAME=> {self.b_name}")

class Student(Course,Branch):
    def __init__(self,uni_name,c_name,b_name,s_name):
        self.s_name=s_name
        super().__init__(uni_name=uni_name,c_name=c_name,b_name=b_name)
    def showDetails(self):
        super().showDetails()
        print(f"STUDENT NAME=> {self.s_name}")

class Faculty(Branch):
    def __init__(self,uni_name,b_name,f_name):
        self.f_name=f_name
        super().__init__(uni_name=uni_name,b_name=b_name)
    def showDetails(self):
        super().showDetails()
        print(f"FACULTY NAME=> {self.f_name}")

c=Course(uni_name="BU",c_name="AI")
c.showDetails()
b=Branch(uni_name="BU",b_name="MCA")
b.showDetails()

print(Student.mro())
s=Student("BU","AI","MCA","Aryan")
s.showDetails()

print(Faculty.mro())
f=Faculty("IIM Bangalore","CS","Mr Singhania")
f.showDetails()