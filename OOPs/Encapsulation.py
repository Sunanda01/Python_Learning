class A1:
    def __init__(self):
        self.__num=100
    def getter(self):
        return(f"{self.__num}")
    def setter(self,num1):
        if(num1<18):
            print("Num should be greater than 18")
        else:
            self.__num=num1
            print(f"New Num=> {self.getter()}")

a1=A1()        
print(f"Current Num=> {a1.getter()}")
a1.setter(15)

a=A1()        
print(f"Current Num=> {a.getter()}")
a.setter(25)

