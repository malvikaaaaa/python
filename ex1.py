class bank:
    def __init__(self,n="nil",l="nil"):
        self.name=n
        self.location=l
    def display(self):
        print("Bank Name:",self.name)
        print("Bank Location:",self.location)

class insurance(bank):
    def __init__(self,n="nil",l="nil",amt=0):
        super().__init__(n,l)
        self.__amount=amt
        
    def display1(self):
        super().display()
        
    def display2(self):
        print("Insurance amount:",self.__amount)

    def __le__(self,other):
        #if(self.__amount<=other.__amount):
            #print("Amount 1 is lesser")
        #else:
            #print("Amount 2 is lesser")
        return(self.__amount<=other.__amount)


bname=input("Enter the bank name:")
bloc=input("Enter the bank location:")
iamt1=int(input("Enter insurance amt 1:"))
iamt2=int(input("Enter insurance amt 2:"))

in1=insurance(bname,bloc,iamt1)
in2=insurance(bname,bloc,iamt2)
in1.display1()
in1.display2()
in2.display2()
if(in1<=in2):
    print("Amount 1 is lesser")
else:
    print("Amount 2 is lesser")
    
#print("Two insurance amount are less than or equal",in1<=in2)

#create class circle(__radius).create class cylinder(height) that inherits from circle.compare 2 cylinders by their volume,overloading >= operator

from math import pi

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @property
    def area(self):
        return pi * self.__radius**2

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.__height = height

    @property
    def height(self):
        return self.__height

    def volume(self):
        return self.area * self.__height

    def __ge__(self, other):
        return self.volume() >= other.volume()

# Example usage:
cylinder1 = Cylinder(radius=3, height=5)
cylinder2 = Cylinder(radius=4, height=6)

if cylinder1 >= cylinder2:
    print("Cylinder 1 has a greater volume than or equal to Cylinder 2.")
else:
    print("Cylinder 1 has a smaller volume than Cylinder 2.")

        

