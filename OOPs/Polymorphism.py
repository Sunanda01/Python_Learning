print(len("Hello"))
print(len([1,2,3,4,5,6,7,8,9,10]))

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

for obj in (a, d, c):
    obj.speak()
