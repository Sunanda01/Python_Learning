from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def display(self,type):
        return(f"Animal Type is {type}")

class Dog(Animal):
    def sound(self):
        print(f"{self.display("Dog")}, It Barks")

class Cat(Animal):
    def sound(self):
        print(f"{self.display("Cat")}, It Mews")
        
d=Dog();
d.sound()

c=Cat();
c.sound()
