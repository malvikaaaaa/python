from graphics import rectangle,circle
from graphics.dgraphics import cuboid,sphere

print("Rectangle")
l=int(input('Length\n'))
b=int(input('Breadth\n'))
print("Area of Rectangle :",rectangle.area(l,b))
print("Perimeter of Rectangle :",rectangle.perimeter(l,b))

print("\nCircle")
r=int(input('Radius\n'))
print("Area of Circle :",circle.area(r))
print("Perimeter of Circle :",circle.perimeter(r))
