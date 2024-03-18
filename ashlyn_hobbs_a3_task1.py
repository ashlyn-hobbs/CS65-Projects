# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# November. 2022

# Task 1: List

# -----------------  subtask 1 -----------------

number = int(input("Enter a number: "))

answer = []

for i in range (2, number):
    
    if number % i == 0:
        answer.append(i)
        
print("Numbers that can fully divide", number, "=", answer)

# -----------------  subtask 2  ------------------

my_list = []

while True:
    
    user_input = int(input("Enter a candidate divisor: "))
    
    if user_input == -1:
        break
    
    my_list.append(user_input)

def eliminate(new_list, num):
    
    new_list = []
    
    for item in my_list:
        if num % item == 0:
            new_list.append(item)
            
    
    return new_list
        

num = int(input("Enter another number: "))

print("List of candidate divisors are: ", my_list)


new_list = eliminate(my_list, num)
        
print("List of divisors are: ", new_list)
# ------------------  subtask 3  -----------------------------

# this function returns the list of indices with invalid color-triplets

def get_invalid_colors():
    
    input_list = [ [100, 0, 0], [40, -156, 0], [0, 156, 0], [40, 156, 500], [0, 0, 250] ]
    
    my_list = []
    
    for i in range (len(input_list)):
        for j in input_list[i]:
            if j < 0 or j > 255:
                my_list.append(i)
            else:
                continue
    print(my_list)
    
get_invalid_colors()

# this function returns the corrected list of color-triplets

def correct_invalid_colors(my_list):
    
    input_list = [ [100, 0, 0], [40, -156, 0], [0, 156, 0], [40, 156, 500], [0, 0, 250] ]
    
    for i in range (len(input_list)):
        for j in input_list[i]:
            if j < 0:
                correct = int(input_list[i].index(j))
                input_list[i][correct] = 0
            elif j > 255:
                correct2 = int(input_list[i].index(j))
                input_list[i][correct2] = 255
            else:
                continue
    print(input_list)

correct_invalid_colors(my_list)

# this function removes the invalid color_triplets

def discard_invalid_colors(my_list):
    
    input_list = [ [100, 0, 0], [40, -156, 0], [0, 156, 0], [40, 156, 500], [0, 0, 250] ]
    
    length = len(input_list)
    
    for i in range (length-2):
        for j in input_list[i]:
            if j < 0:
                input_list.pop(i)
            elif j > 255:
                input_list.pop(i)
            else:
                continue
    print(input_list)
    
discard_invalid_colors(my_list)
    
    
