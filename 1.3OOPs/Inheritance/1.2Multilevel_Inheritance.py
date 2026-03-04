class Grandparent:
    def show_grandparent(self):
        print("Grandparent method")

class Parent(Grandparent):
    def show_parent(self):
        print("Parent method")

class Child(Parent):
    def show_child(self):
        print("Child method")

c = Child()
c.show_grandparent()
c.show_parent()
c.show_child()

class Grandparent:
    def __init__(self):
        print("Grandparent constructor")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

c = Child()

class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

c = Child()
c.greet()

class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet(self):
        super().greet()
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()
print(Child.mro())

