'''from graphics import rectangle,circle
from graphics.dgraphics import cuboid,sphere'''

'''from graphics import rectangle as r
import graphics.circle
from graphics.dgraphics import cuboid,sphere'''

from graphics import *


print("Rectangle")
l=int(input('Length\n'))
b=int(input('Breadth\n'))
print("Area of Rectangle :",rectangle.area(l,b))
print("Perimeter of Rectangle :",rectangle.perimeter(l,b))

print("\nCircle")
r=int(input('Radius\n'))
print("Area of Circle :",circle.area(r))
print("Perimeter of Circle :",circle.perimeter(r))

print("\nCuboid")
l=int(input('Length\n'))
print("Area of Cuboid :",cuboid.area(l))
print("Volume of Cuboid :",cuboid.volume(l))

print("\nSphere")
r=int(input('Radius\n'))
print("Area of Sphere :",sphere.area(r))
print("Volume of Sphere :",sphere.volume(r))
