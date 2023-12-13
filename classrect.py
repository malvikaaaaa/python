class Rectangle:
    def __init__(self,length=0,breadth=0):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    def __eq__(self,other):
        return self.length*self.breadth==other.length*other.breadth


r1=Rectangle(4,3)
r2=Rectangle(6,2)
print("Object 1")
print("-->Area:",r1.area())
print("-->Perimeter:",r1.perimeter())
print("Object 2")
print("-->Area:",r2.area())
print("-->Perimeter:",r2.perimeter())
print("Areas are equal:",r1==r2)
