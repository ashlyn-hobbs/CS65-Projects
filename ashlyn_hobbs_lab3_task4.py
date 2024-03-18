from graphics import *


def create_rect_circ_mouseclick():
    window = GraphWin("Mouse Interaction", 400, 400)
    
    # Mouse User Interaction
    mouse_point1 = window.getMouse()
    mouse_point2 = window.getMouse()
    
    print(mouse_point1)
    print(mouse_point2)
    
    # create circ using user mouse points
    my_cir     = Circle(mouse_point1, 100)
    my_cir.setFill("red")
    
    my_cir.draw(window)
    
    # create rect using user mouse points
    
    rect   = Rectangle(mouse_point1, mouse_point2)
    rect.setFill("blue")
    rect.draw(window)
    
    
    return window

w1 = create_rect_circ_mouseclick()