#Write a python program that has a class named circle , use a class variable to define the values of a constaant pi.Use this class variable to calculate area and circumference of a circle with specified radius where radius=7.5

'''method-1'''

class Circle:
    pi=3.14159
    def __init__(self,r):
        area=Circle.pi*r*r
        circumference=2*Circle.pi*r
        print("Area of circle is:",area)
        print("Circumference of circle is:",circumference)
n=Circle(7.5)





'''method-2'''
class Circle:
    pi=3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
            return Circle.pi*self.r*self.r
    def circum(self):
            return 2*Circle.pi*self.r
n=Circle(7.5)
print("Area is:", n.area())
print("Circumference is:", n.circum())

