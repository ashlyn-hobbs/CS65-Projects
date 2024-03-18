# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# October, 2022

# this program will prompt the user to enter two numbers for an operation of their choice

# this user defined function adds two numbers
def add_numbers(num1, num2):
    res1 = num1 + num2
    
    return res1
    
# this user defined function subtracts second number from the first
def subtract_numbers(num1, num2):
    res2 = num1 - num2
    
    return res2
    
# this user defined function multiplies two numbers
def multiply_numbers(num1, num2):
    res3 = num1 * num2
    
    return res3
    
# this user defined function divides two numbers
def divide_numbers(num1, num2):
    res4 = num1 // num2
    
    return res4

# this user defined function computes the power fo first number by the second number
def power_numbers(num1, num2):
    res5 = num1 ** num2
    
    return res5
    
# this user defined function computes the remainder of the first number by the second
def modulus_numbers(num1, num2):
    if num1 < 0:
        num1 = num1*(-1)
    if num2 < 0:
        num2 = num2*(-1)
    res6 = num1 % num2
    
    return res6

def print_menu():
    print("----------------------------------------------------------------------------------------------------")
    print("                       Menu: Revisiting simple arithmetic operations                                ")
    print("----------------------------------------------------------------------------------------------------")
    print("1) Enter 'add'      or 'ADD'      to find the summation between two numbers                         ")
    print("2) Enter 'subtract' or 'SUBTRACT' to find the difference between the two numbers                    ")
    print("3) Enter 'multiply' or 'MULTIPLY' to find the multiplication between the two numbers                ")
    print("4) Enter 'divide'   or 'DIVIDE'   to find the division of a number by the 2nd one                   ")
    print("5) Enter 'power'    or 'POWER'    to find the result of 1st number raised to the power of 2nd number")
    print("6) Enter 'modulus'  or 'MODULUS'  to find the remainder of the 1st number by the 2nd number         ")
    print("----------------------------------------------------------------------------------------------------")
    return None

# prompts the user to enter their choice of artimetic operation along with two numbers
def main():
    
    print_menu()
    user_choice = input("Enter your choice from the list above: ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # user choices and calling their functions
    if user_choice == 'add':
        print("Result of addition operation  ", add_numbers(num1, num2))
    elif user_choice == 'ADD':
        print("Result of addition operation  ", add_numbers(num1, num2))
    elif user_choice == 'subtract':
        print("Result of subtraction operation  ", subtract_numbers(num1, num2))
    elif user_choice == 'SUBTRACT':
        print("Result of subtraction operation  ", subtract_numbers(num1, num2))
    elif user_choice == 'multiply':
        print("Result of multiplication operation  ", multiply_numbers(num1, num2))
    elif user_choice == 'MULTIPLY':
        print("Result of multiplication operation  ", multiply_numbers(num1, num2))
    elif user_choice == 'power':
        print("Result of power operation  ", power_numbers(num1, num2))
    elif user_choice == 'POWER':
        print("Result of power operation  ", power_numbers(num1, num2))
    elif user_choice == 'divide' and num2 == 0:
        print("ERROR: divide by zero")
    elif user_choice == 'DIVIDE' and num2 == 0:
        print("ERROR: divide by zero")
    elif user_choice == 'DIVIDE' and num2 != 0:
        print("Result of division operation  ", divide_numbers(num1, num2))
    elif user_choice == 'divide' and num2 != 0:
        print("Result of division operation  ", divide_numbers(num1, num2))
    elif user_choice == 'modulus':
        print("Result of modulus operation  ", modulus_numbers(num1, num2))
    elif user_choice == 'MODULUS':
        print("Result of modulus operation  ", modulus_numbers(num1, num2))
    else:
        print("Choice not listed above ... ")
        
    return None

main()
                   
