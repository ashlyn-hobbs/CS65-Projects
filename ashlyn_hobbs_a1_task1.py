# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# October, 2022

# this program will incorporate user input and draw one of three shapes at a random location

from graphics import *
import random

# coordinates code
ranx = random.randint(1, 400)
rany = random.randint(1, 400)

# draws a colorful circle at a random point with a radius of 100
def draw_circle(window):
    
    #create circle
    cir_center = Point(ranx, rany)
    cir_radius = 100
    my_cir     = Circle(cir_center, cir_radius)
    my_cir.setFill("blue")
    
    my_cir.draw(window)
    
    return None

# draws a colorful rectangle at a random point
def draw_rectangle(window):
    
    x2 = 75
    y2 = 75
    
    point1 = Point(ranx ,rany)
    point2 = Point(x2, y2)
    
    rect   = Rectangle(point1, point2)
    rect.setFill("red")
    rect.draw(window)
    
    return None

# draws a colorful triangle at a random point
def draw_triangle(window):
     
    xleft = 100
    xright = 230
    yleft = 115
    yright = 200
    point1 = Point(ranx, rany)
    point2 = Point(xleft, yleft)
    point3 = Point(xright, yright)
    
    poly    = Polygon(point1, point2, point3)
    poly.setFill("green")
    poly.draw(window)
    
    return None

def print_menu():
    print("-------------------------------------------------------------------------------------------")
    print("                 Menu: Revisiting circle, rectangle, and triangle drawing                  ")
    print("-------------------------------------------------------------------------------------------")
    print("1) Enter 'circle' or 'Circle' or 'CIRCLE' to draw a circle at a random location")
    print("2) Enter 'rectangle' or 'Rectangle' or RECTANGLE' to draw a rectangle at a random location")
    print("3) Enter 'triangle' or 'Triangle' or 'TRIANGLE' to draw a triangle at a random location")
    print("-------------------------------------------------------------------------------------------")
    return None

# prompts the user to enter their desired shape and then proceeds to draw that shape in a random location
def main():
    
    print_menu()
    window = GraphWin("New window", 400, 400)
    user_choice = input("Enter the name of your shape from the list above: ")
    # user chooses circle
    if user_choice == 'circle':
        draw_circle(window)
    elif user_choice == 'Circle':
        draw_circle(window)
    elif user_choice == 'CIRCLE':
        draw_circle(window)
    # user chooses rectangle
    elif user_choice == 'rectangle':
        draw_rectangle(window)
    elif user_choice == 'Rectangle':
        draw_rectangle(window)
    elif user_choice == 'RECTANGLE':
        draw_rectangle(window)
    # user chooses triangle
    elif user_choice == 'triangle':
        draw_triangle(window)
    elif user_choice == 'Triangle':
        draw_triangle(window)
    elif user_choice == 'TRIANGLE':
        draw_triangle(window)
    else:
        print("Try reading the options again!")
    
    
    return window

main()