# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# October, 2022

# Subtask 1: print a special character N times using for loop
def print_menu():
    print("-----------------------------")
    print("     @     #     $     *     ")
    print("-----------------------------")
    return None

def main():
    print_menu()
    character = input("Enter one of the special characters above: ")
    N = int(input("Enter an integer number: "))
    
    for vari in range (N):
        print(character, end="")
    return None

main()
print("                                              ")

# Subtask 2: summation of multiples of 5s using for loop

given = int(input("Enter one integer number: "))

total = 0
for number in range (1, given+1):
    if (number % 5 == 0):
        total = total + number
print(total)

# Subtask 3: finding a number in a list using for loop

my_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 22, 24, 26, 26, 28]

usernum = int(input("Enter one integer number: "))

num_found = False
for val in my_list:
    if (val == usernum):
        num_found = True  # fix the code for when the user enters a num not in the list
if (num_found):
    print("FOUND")
else:
    print("NOT FOUND")

# Subtask 4: counting frequency of number using for loop

new_list = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]

one_num = int(input("Enter one integer number: "))

count = 0

for item in new_list:
    if (item == one_num):
        count = count + 1
        
print(one_num, "appears", count, "times in the list.")

# Subtask 5: finding location of a number in a list using for loop

location_num = int(input("Enter one integer number: "))

for i in range(len(my_list)):
    if my_list[i] == location_num:
        print(location_num, "appears at location", str(i))
    else:
        pass

# Subtask 6: find the max and min numbers in a list using for loop

the_list = [10, 3, 15, -7, 90, 11]

maxVal = the_list[0]
minVal = the_list[0]

for var in the_list:
    if var > maxVal:
        maxVal = var
print("Maximum Number is ", maxVal)

for var in the_list:
    if var < minVal:
        minVal = var
print("Minimum Number is ", minVal)


    
        


