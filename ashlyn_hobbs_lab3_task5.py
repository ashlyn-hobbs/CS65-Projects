from graphics import *

def draw_one_rectangle(x1, y1, x2, y2, color, window):
    
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    rect   = Rectangle(point1, point2)
    rect.setFill(color)
    rect.draw(window)
    
    return None


def build_staircase():
    
    window = GraphWin("Staircase", 400, 400)
    window.setCoords(0, 0, 400, 400)
    
    x1 = 0
    y1 = 0
    x2 = 100
    y2 = 100
    
    
    draw_one_rectangle(x1, y1, x2, y2, "blue", window)
    draw_one_rectangle(x1+100, y1+100, x2+100, y2+100, "red", window)
    draw_one_rectangle(x1+200, y1+200, x2+200, y2+200, "blue", window)
    draw_one_rectangle(x1+300, y1+300, x2+300, y2+300, "red", window)
    
    
    return window

build_staircase()
    