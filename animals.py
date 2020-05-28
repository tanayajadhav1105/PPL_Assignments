#The purpose of this program is to show abstraction, encapsulation,public and private access specifiers.


from abc import ABC

# Animals is an abstract class and it cant be instantiated
# Abstraction helps in hiding the methods used by programmer to work with the data.
# Private and Public members are shown below. Private members have _ prefix.

class Animals(ABC):
    def basic(self):
        self._eyes=2          #_eyes __ears __nose and __legs
        self._limbs=4          #are private variables and cannot be accesed directly
        self._ears=2
        self._nose=1
    def print_characters(self):
        print("It has ",self._eyes," eyes.")
        print("It has ",self._ears," ears.")
        print("It has ",self._nose," nose.")
        print("It has ",self._limbs," limbs.")

#Encapsulation is the restriction of access to certain variables.
class Wild_animals(Animals):
    def __init__(self):
        super().basic()
        self.home="Forest"
    def print_characters(self):
        super().print_characters()
        print("It is a wild animal.")
        print("It lives in the "+self.home+".")


class Domestic_animals(Animals):
    def __init__(self):
        super().basic()
        self.home="Human Neighbourhood"
    def print_characters(self):
        super().print_characters()
        print("It is a domestic animal.")
        print("It lives in the "+self.home+".")



#Wild Animals

class Lion(Wild_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Ochre and brown"
    def print_characters(self):
        print("This is a Lion named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It has brown hair around its head.")


class Tiger(Wild_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Orange and Black"
    def print_characters(self):
        print("This is a Tiger named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It has black stripes.")


class Giraffe(Wild_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Yellow and Brown"
    def print_characters(self):
        print("This is a Giraffe named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It has very long neck.")


class Fox(Wild_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Orange"
    def print_characters(self):
        print("This is a Fox named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It is said to be cunning.")


class Cheetah(Wild_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Ochre"
    def print_characters(self):
        print("This is a Cheetah named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It is the fastest animal.")


#Domestic Animals

class Cat(Domestic_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Black"
    def print_characters(self):
        print("This is a Cat named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It drinks milk.")

class Dog(Domestic_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="White"
    def print_characters(self):
        print("This is a Dog named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It is human's most loyal friend.")



class Cow(Domestic_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="White and Black"
    def print_characters(self):
        print("This is a Cow named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It gives milk for our daily needs.")


class Donkey(Domestic_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="Gray"
    def print_characters(self):
        print("This is a Donkey named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It is hardworking.")


class Sheep(Domestic_animals):
    def __init__(self,name):
        super().__init__()
        self.name=name
        self.color="White and Black"
    def print_characters(self):
        print("This is a Sheep named "+self.name+".")
        super().print_characters()
        print("It is "+self.color+" in color.")
        print("It gives wool for sweaters.")



if __name__=='__main__':
    print("Animal Kingdom")
    wild=[Lion,Tiger,Giraffe,Fox,Cheetah]
    domestic = [Cat, Dog, Cow, Donkey, Sheep]
    while True:
        print("\nEnter choice of type of  animal. Options are:")
        print("1.Wild Animals\n2.Domestic Animals\n3.Exit\n")
        n=int(input())
        if n==1:
            print("Enter choice animal. Options are:")
            print("1.Lion\n2.Tiger\n3.Giraffe\n4.Fox\n5.Cheetah\n")
            a=int(input())
            a=wild[a-1]
            name=input("Enter name : ")
            b=a(name)
            b.print_characters()
        if n==2:
            print("Enter choice animal. Options are:")
            print("1.Cat\n2.Dog\n3.Cow\n4.Donkey\n5.Sheep\n")
            a=int(input())
            a=domestic[a-1]
            name=input("Enter name : ")
            b=a(name)
            b.print_characters()
        if n==3:
            break




