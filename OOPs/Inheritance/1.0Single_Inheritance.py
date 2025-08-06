class Animal:
    def __init__(self):
        self.lifeSpan=15
        self.nature='kind'
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def __init__(self,name,age):
        super().__init__()
        self.name=name
        self.age=age
    def bark(self):
        super().speak()
        print(f"{self.name} Barks")
    def display(self):
        print(f"Name\t{self.name}\nAge\t{self.age} years\nLifeSpan\t{self.lifeSpan} years\nNature\t{self.nature}\n\n")

puppy=Dog('Shiru',1)
puppy.bark()
puppy.display()

pup=Dog('Tommy',2)
pup.display()
# print(f"Name\t{puppy.name}\nAge\t{puppy.age} years\nLifeSpan\t{puppy.lifeSpan} years\nNature\t{puppy.nature}")
