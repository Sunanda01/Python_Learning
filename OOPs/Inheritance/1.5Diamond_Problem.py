class GrandParent:
    def __init__(self,bloodGrp):
        self.bloodGrp=bloodGrp
    def display(self):
        print(f"GrandParent BloodGroup=> {self.bloodGrp}")

class Parent1(GrandParent):
    def __init__(self,bloodGrp,p1_bloodGrp):
        super().__init__(bloodGrp)
        self.p1_bloodGrp=p1_bloodGrp
    def display(self):
        super().display()
        print(f"Parent1 BloodGroup=> {self.p1_bloodGrp}")

class Parent2(GrandParent):
    def __init__(self,bloodGrp,p2_bloodGrp):
        super().__init__(bloodGrp)
        self.p2_bloodGrp=p2_bloodGrp
    def display(self):
        super().display()
        print(f"Parent2 BloodGroup=> {self.p2_bloodGrp}")

class Child(Parent1,Parent2):
    def __init__(self,bloodGrp,p1_bloodGrp,p2_bloodGrp,c_bloodGrp):
        super().__init__(bloodGrp,p1_bloodGrp,p2_bloodGrp)
        self.c_bloodGrp=c_bloodGrp
    def display(self):
        super().display()
        print(f"Child BloodGroup=> {self.c_bloodGrp}")
        
p1=Parent1('A+','O+')
p1.display()
p2=Parent2('A+','A+')
p2.display()
#Below Code will not work
c1=Child('A+','O+','O+','A+')
c1.display()