from graphics import *

xtop = int(input("What is the x-coordinate of the top corner: "))
ytop = int(input("What is the y-coordinate of the top corner: "))
xleft = int(input("What is the x-coordinate of the left corner: "))
yleft = int(input("What is the y-coordinate of the left corner: "))
xright = int(input("What is the x-coordinate of the right corner: "))
yright = int(input("What is the y-coordinate of the right corner: "))

def create_simple_window_triangle():
    window = GraphWin("Window: Triangle", 400, 400)
    
    point1 = Point(xtop, ytop)
    point2 = Point(xleft, yleft)
    point3 = Point(xright, yright)
    
    poly    = Polygon(point1, point2, point3)
    poly.setFill("blue")
    poly.draw(window)
    
    return window

win_default = create_simple_window_triangle()