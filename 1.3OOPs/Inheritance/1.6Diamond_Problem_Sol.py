class GrandParent:
    def __init__(self,bloodGrp):
        self.bloodGrp=bloodGrp
    def display(self):
        print(f"4 GrandParent BloodGroup=> {self.bloodGrp}")

class Parent1(GrandParent):
    def __init__(self,p1_bloodGrp,**kwargs):
        super().__init__(**kwargs)
        self.p1_bloodGrp=p1_bloodGrp
    def display(self):
        super().display()
        print(f"2 Parent1 BloodGroup=> {self.p1_bloodGrp}")

class Parent2(GrandParent):
    def __init__(self,p2_bloodGrp,**kwargs):
        super().__init__(**kwargs)
        self.p2_bloodGrp=p2_bloodGrp
    def display(self):
        super().display()
        print(f"3 Parent2 BloodGroup=> {self.p2_bloodGrp}")

class Child(Parent1,Parent2):
    def __init__(self,bloodGrp,p1_bloodGrp,p2_bloodGrp,c_bloodGrp):
        super().__init__(bloodGrp=bloodGrp,p1_bloodGrp=p1_bloodGrp,p2_bloodGrp=p2_bloodGrp)
        self.c_bloodGrp=c_bloodGrp
    def display(self):
        super().display()
        print(f"1 Child BloodGroup=> {self.c_bloodGrp}")
        
p1=Parent1(bloodGrp='A+',p1_bloodGrp='O+')
p1.display()
p2=Parent2(bloodGrp='A+',p2_bloodGrp='A+')
p2.display()

print(Child.mro())
c1=Child(bloodGrp='A+',p1_bloodGrp='O+',p2_bloodGrp='A+',c_bloodGrp='A+')
c1.display()