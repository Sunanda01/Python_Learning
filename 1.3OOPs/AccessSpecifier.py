#Protected
class A:
    def __init__(self):
        self._num=30
class B(A):
    def display(self):
        print(self._num)

b=B()
print(b._num)
b._num=100
print(b._num)
b.display()

#Private
class A1:
    def __init__(self):
        self.__name
class B1:
    def dis(self):
        print(self.__name)
# a=A()        
# print(a.__name)
# b=B1()
# b.dis()

class A:
    def __init__(self):
        self.__data = "A"

class B(A):
    def __init__(self):
        super().__init__()
        self.__data = "B"  # Won’t override A’s __data due to name mangling
