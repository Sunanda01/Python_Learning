import math
PI=3.14
class Cicle:
    def __init__(self,radius):
        self.radius=radius
    def area_circumference(self):
        area=PI*(self.radius**2)
        circumference=2*PI*self.radius
        return {'area':area,'circumference':circumference}
    
radius=float(input("Enter radius of a circle=>\t"))
circle1=Cicle(radius)
result=circle1.area_circumference()
print(f"Radius={radius} Area={round(result['area'],2)} Circumference={round(result['circumference'],2)}")

