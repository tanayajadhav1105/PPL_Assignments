#The purpose of this program is to show abstraction, encapsulation,public and private access specifiers.

from math import *
from abc import ABC

#Class Shapes is an abstract class. The user thus, cannot see how fill and color functions work.
#This is called Abstraction

#Encapsulation is restriction of access of data and methods. In this case, __area is not accessible outside class.

#All members of classes are public except _area, which as '_' prefix and is private
#Diamond and Parallelogram need their own init function as __area is not inherited.


class Shapes(ABC):
    def print_basic(self):
        print("This is a geometric shape.")


class square(Shapes):
    def __init__(self,s):
        self.s=s
        self.area=self.s*self.s
        self.peri=4*self.s
    def print_characters(self):
        super().print_basic()
        print("You chose a square.")
        print("It has 4 sides of the same length with 90deg angle between them.")
        print("Its 3D shape is called a cube")
        print("Its perimeter is : "+str(self.peri)+"units.")
        print("Its area is : "+str(self.area)+" sq. units.")

class rectangle(Shapes):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area=self.l*self.b
        self.peri=2*(self.l+self.b)
    def print_characters(self):
        super().print_basic()
        print("You chose a rectangle.")
        print("It has 4 sides with opposite sides of same length with 90deg angle between them.")
        print("Its 3D shape is called a cuboid")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")

class circle(Shapes):
    def __init__(self,r):
        self.r=r
        self.area=3.14*self.r*self.r
        self.peri=2*3.14*self.r
    def print_characters(self):
        super().print_basic()
        print("You chose a circle.")
        print("It has doesnt have any sides but infinite points located at fixed distance from the circle.")
        print("Its 3D shape is called a sphere")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")

class triangle(Shapes):
    def __init__(self,s):
        self.s=s
        self.area=(sqrt(3)/4)*self.s*self.s
        self.peri=3*self.s
    def print_characters(self):
        super().print_basic()
        print("You chose an Equilateral triangle.")
        print("It has 3 sides of same length with 60deg angle between them.")
        print("Its 3D shape is called a triangular pyramid")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")

class hexagon(Shapes):
    def __init__(self,s):
        self.s=s
        self.area=((3*sqrt(3))/4)*self.s*self.s
        self.peri=6*self.s
    def print_characters(self):
        super().print_basic()
        print("You chose a regular hexagon.")
        print("It has 6 sides equal in length.")
        print("It can be divided in to 6 equilateral triangles")
        print("Its perimeter is : "+str(self.peri)+"units.")
        print("Its area is : "+str(self.area)+" sq. units.")

class oval(Shapes):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.area=3.14*self.a*self.b
        self.peri=2*3.14*(sqrt(((self.a*self.a)+(self.b*self.b))/2))
    def print_characters(self):
        super().print_basic()
        print("You chose an oval.")
        print("It has 2 focii point such that sum of distances of any point on the oval from focii is constant.")
        print("It has a major axis and minor axis.")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")

class parallelogram(Shapes):
    def __init__(self,l,b,h):
        self.l=l
        self.h=h
        self.b=b
        self.area=self.l*self.h
        self.peri=2*(self.l+self.b)
    def print_characters(self):
        super().print_basic()
        print("You chose a parallelogram.")
        print("It has 4 sides with opposite sides equal and angle between them not necessarily 90deg.")
        print("all rectangles are parallelograms.")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")

class rhombus(Shapes):
    def __init__(self,s,h):
        self.s=s
        self.h=h
        self.area=self.s*self.h
        self.peri=4*self.s
    def print_characters(self):
        super().print_basic()
        print("You chose a rhombus.")
        print("It has 4 sides of same length and angle between them is not necessarily 90deg.")
        print("All squares are rhombus.")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")

class kite(Shapes):
    def __init__(self,d1,d2,s1,s2):
        self.d1=d1
        self.d2=d2
        self.s1=s1
        self.s2=s2
        self.area=0.5*self.d1*self.d2
        self.peri=2*(self.s1+self.s2)
    def print_characters(self):
        super().print_basic()
        print("You chose a Kite.")
        print("It has 4 sides with pairs of adjacent sides equal.")
        print("Its diagonals are perpendicular to each other.")
        print("Its perimeter is : " + str(self.peri) + "units.")
        print("Its area is : " + str(self.area) + " sq. units.")


if __name__=="__main__":
    print("World of shapes\n")
    while True:
        i=int(input("\nEnter your choice:\n1.Square\n2.Rectangle\n3.Circle\n4.Tringle\n5.Hexagon\n6.Oval\n7.Parallelogram\n8.Rhombus\n9.Kite\n10.Exit\n"))

        if i==1:
            s=int(input("Enter side : "))
            c=square(s)
            c.print_characters()
        elif i==2:
            l=int(input("Enter length : "))
            b=int(input("Enter breadth : "))
            c=rectangle(l,b)
            c.print_characters()
        elif i==3:
            r=int(input("Enter radius : "))
            c=circle(r)
            c.print_characters()
        elif i==4:
            s=int(input("Enter Side : "))
            c=triangle(s)
            c.print_characters()
        elif i==5:
            s=int(input("Enter Side : "))
            c=hexagon(s)
            c.print_characters()
        elif i==6:
            a=int(input("Enter major axis : "))
            b=int(input("Enter minor axis : "))
            c=oval(a,b)
            c.print_characters()
        elif i==7:
            l=int(input("Enter length : "))
            b=int(input("Enter base : "))
            h=int(input("Enter height : "))
            c=parallelogram(l,h,b)
            c.print_characters()
        elif i==8:
            s=int(input("Enter side : "))
            h=int(input("Enter height : "))
            c=rectangle(s,h)
            c.print_characters()
        elif i==9:
            d1=int(input("Enter diagonal1 : "))
            d2=int(input("Enter diagonal2 : "))
            s1 = int(input("Enter side1 : "))
            s2=int(input("Enter side2 : "))
            c=kite(d1,d2,s1,s2)
            c.print_characters()
        elif i==10:
            break






