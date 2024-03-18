# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# October, 2022

# Subtask 1: find the summation of all the numbers from 1 up to user given number
total = 0

last_num = int(input("Enter one integer number: "))

first_num = 1

while first_num <= last_num:
    
    total = total + first_num
    
    first_num = first_num + 1
    
print("Summation: ", total)
# Subtask 2: find the summation of all the odd numbers from 1 up to user given number
odd_total = 0

seclast_num = int(input("Enter one integer number: "))

first_num = 1

while first_num <= seclast_num:
    
    if (first_num % 2 != 0):
        odd_total = odd_total + first_num
        
    first_num = first_num + 1
        
print(odd_total)

# Subtask 3: Find regional state using while loop and user input
def print_menu():
    print("------------------------------------")
    print("     DE,     NC,     NJ,     VA     ")
    print("     IA,     IN,     KS,     WI     ")
    print("     TX,     LA,     AL,     AK     ")
    print("     CA,     OR,     WA,     NV     ")
    print("------------------------------------")
    return None

def main():
    print_menu()
    state = input("Enter the name of a state from the options above: ")
    
    while state != "END":
        
        if state == 'DE' or state == 'NC' or state == 'NJ' or state == 'VA':
            print("Eastern")
        elif state == 'IA' or state == 'IN' or state == 'KS' or state == 'WI':
            print("Midwestern")
        elif state == 'TX' or state == 'LA' or state == 'AL' or state == 'AK':
            print("Southern")
        elif state == 'CA' or state == 'OR' or state == 'WA' or state == 'NV':
            print("Eastern")
        else:
            print("wrong choice ...")
        return None

main()
            
            
        
    
