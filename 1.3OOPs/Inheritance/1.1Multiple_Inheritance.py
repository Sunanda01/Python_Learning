class Animal:
    def __init__(self,nature):
        self.nature=nature
    def checkOrder(self):
        print("Animal Parent")


class DomesticAnimal:
    def __init__(self):
        self.lifeSpan=15
    def speak(self):
        print("Animal Speaks")
    def checkOrder(self):
        print("DomesticAnimal Parent")

class Dog(Animal,DomesticAnimal):
    def __init__(self,name,age,nature):
        Animal.__init__(self,nature)
        DomesticAnimal.__init__(self)
        self.name=name
        self.age=age
    def bark(self):
        super().speak()
        print(f"{self.name} Barks")
    def display(self):
        print(f"Name\t{self.name}\nAge\t{self.age} years\nLifeSpan\t{self.lifeSpan} years\nNature\t{self.nature}\n\n")
    # def checkOrder(self):
    #     print("Dog Child")          #Dog Child


puppy=Dog('Shiru',1,'friendly')
puppy.bark()
puppy.display()

pup=Dog('Tommy',2,'aggressive')
pup.display()

DomesticAnimal.checkOrder(puppy)    #DomesticAnimal Parent
puppy.checkOrder()      #Animal Parent
print(Dog.__mro__)
# print(f"Name\t{puppy.name}\nAge\t{puppy.age} years\nLifeSpan\t{puppy.lifeSpan} years\nNature\t{puppy.nature}")
