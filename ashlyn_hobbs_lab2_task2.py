#_______________________________________  Task 2  ___________________________________________

from graphics import *
from math import pi

# stats for rectangle
def computer_rectangle_stats(length, width):

     area = length * width
     perimeter = (length*2 + width*2)

     return area, perimeter
     
a = 15
b = 22
area, perimeter = computer_rectangle_stats(a, b)
print("rectangle length =", a, ", width =", b)
print("Area of the rectangle is ", area, " and perimeter ", perimeter)

# stats for square
def computer_square_stats(length, width):
    
     area = length * width
     perimeter = (length*2 + width*2)

     return area, perimeter

c = 10
d = 10
area, perimeter = computer_square_stats(c, d)
print("square length =", c, ", width =", d)
print("Area of the square is ", area, " and perimeter ", perimeter)

# stats for equilateral triangle
def computer_triangle_stats(base, height):

     area = (base * height)//2
     perimeter = base*3
     
     return area, perimeter
    
e = 6
f = 8
area, perimeter = computer_triangle_stats(e, f)
print("triangle sides length =", e, ", height =", f)
print("Area of the triangle is ", area, " and perimeter ", perimeter)

# stats for circle
def computer_circle_stats(radius):
    
    value_of_pi = pi
    area = (value_of_pi)*(radius*radius)
    perimeter = (value_of_pi)*(radius*2)
    
    return area, perimeter

g = 7
area, perimeter = computer_circle_stats(g)
print("circle radius =", g)
print("Area of the circle is ", round(area, 2), " and perimeter ", round(perimeter,2))
