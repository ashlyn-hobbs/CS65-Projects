# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# October, 2022

# Subtask 1: building a rectangle

side1 = int(input("Enter the height of the rectangle: "))
side2 = int(input("Enter the width of the rectangle: "))

for i in range(side1):
    for j in range(side2):
        print("*", end="")
    print()

# Subtask 2: building a right-facing right-triangle

trilength = int(input("Enter the length of the right triangle's adjacent/opposite sides: "))

for i in range(trilength):
    for j in range(i+1):
        print("*", end="")
    print()
    
# Subtask 3: building a left-facing right-triangle

lentriangle = int(input("Enter the length of the right trianngle's adjacent/opposite sides: "))

for row in range(1, lentriangle+1):
    # Display Space
    for space in range(1, (lentriangle-row)+1):
        print(" ", end="")
    # Display *
    for star in range(1, row+1):
        print("*", end="")
    print()