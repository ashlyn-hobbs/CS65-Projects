# Author's name: Ashlyn Hobbs
# Author's contact: ashlyn.hobbs@drake.edu
# Date: (September 1, 2022)
# Collaborator:
#   I did this individually

print("Yay! this is my first python program in CS65!")


#--------------------------    Task 1  -------------------------     
# add, multiplication, divide, etc arithmetic operation
print(25+64)
print(13*3)
print(225/4)  #This operation will directly divide the numbers and include the decimals if there are any
print(225//4)  #This operation will divide the numbers and round to the nearest number while leaving no decimals
print(15 % 4)
print(3**7)
#--------------------------    Task 2    ------------------------
# variables

time_sec = 60
temp_degree = 27

mile_to_kilometer = 1.609
price_in_dollars = 1500.89

first_name = 'Fiona '
last_name = "Johnson"

num_of_miles = 4
num_of_kilometers = num_of_miles*mile_to_kilometer
print(num_of_miles, "miles equal to", num_of_kilometers, "kilometers")

full_name = (first_name + last_name)

print(full_name)




#--------------------------    Task 3     ------------------------
# user input

height = input("Enter the height of the wall (in inches): ")


print("The wall is ", (int(height)/12), "feet tall")