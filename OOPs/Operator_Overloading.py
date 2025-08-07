class ComplexNum:
    def __init__(self,r,i):
        self.r=r
        self.i=r
    def __add__(self,other):
        return(f"{self.r+other.r} + {self.i+other.i}i")
c1=ComplexNum(5,7)
c2=ComplexNum(7,5)
print(c1+c2)

#In this code we cant compare objects directly so for this we r using operator overloading
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def display(self,other):
        if(self.age>other.age):
            return self.age
        else:
            return other.age       
  
p1=Person("Rounak",26)
p2=Person("Sunanda",24)
print(Person.display(p1,p2))

class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def __gt__(self,other):
        if(self.age>other.age):
            return self.name
        else:
            return other.name

p1=Person("Rounak",26)
p2=Person("Sunanda",24)
print(f"{p1>p2} will pay the Bill")