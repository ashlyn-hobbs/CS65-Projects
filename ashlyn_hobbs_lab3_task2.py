from graphics import *

xleft = int(input("What is the x-coordinate of the left corner: "))
yleft = int(input("What is the y-coordinate of the left corner: "))
xright = int(input("What is the x-coordinate of the right corner: "))
yright = int(input("What is the y-coordinate of the right corner: "))

def create_simple_window_w_rect():
    window = GraphWin("Window: Rectangle", 400, 400)
    
    point1 = Point(xleft,yleft)
    point2 = Point(xright, yright)
    
    rect   = Rectangle(point1, point2)
    rect.setFill("blue")
    rect.draw(window)
    
    return window

w1 = create_simple_window_w_rect()