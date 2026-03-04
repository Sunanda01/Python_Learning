class Dog:
    def speak(self):
        print("Bark!")

class Cat:
    def speak(self):
        print("Meow!")

def animal_sound(animal):
    animal.speak()

dog = Dog()
cat = Cat()

animal_sound(dog)  # Bark!
animal_sound(cat)  # Meow!
