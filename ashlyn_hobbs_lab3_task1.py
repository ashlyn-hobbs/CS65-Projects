from graphics import *

xcen = int(input("What is the x-coordinate of the center: "))
ycen = int(input("What is the y-coordinate of the center: "))
rad  = int(input("What is the radius of the circle      : "))


def create_circle_default_coord():
    
    window = GraphWin("Default coord. system", 400, 400)
    
    #create circle
    cir_center = Point(xcen, ycen)
    cir_radius = rad
    my_cir     = Circle(cir_center, cir_radius)
    my_cir.setFill("blue")
    
    my_cir.draw(window)
    
    return window

# You can tell the difference between the two variables bc they are clearly labled differently
# The term 'window' is a local-variable because it is defined within the function
# the term 'win_default' is a global variable because it is defined outside of the function
win_default = create_circle_default_coord()