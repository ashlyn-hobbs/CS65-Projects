#____________________________  Task 3   ____________________________

import math

a = input("Enter the x-coordinate of your start position: ")
b = input("Enter the y-coordinate of your start position: ")
c = input("Enter the x-coordinate of your end position: ")
d = input("Enter the y-coordinate of your end position: ")

print("distance between the two locations is ", (math.sqrt(((((int(c)) - (int(a)))**2)) + (((int(d)) - (int(b)))**2))))
print("Integer part of the distance: ", int(math.sqrt(((((int(c)) - (int(a)))**2)) + (((int(d)) - (int(b)))**2))))
print("Rounding the distance makes it: ", round(math.sqrt(((((int(c)) - (int(a)))**2)) + (((int(d)) - (int(b)))**2))))
print("Flooring the distance makes it: ", math.floor(math.sqrt(((((int(c)) - (int(a)))**2)) + (((int(d)) - (int(b)))**2))))
print("Ceiling the distance makes it: ", math.ceil(math.sqrt(((((int(c)) - (int(a)))**2)) + (((int(d)) - (int(b)))**2))))
