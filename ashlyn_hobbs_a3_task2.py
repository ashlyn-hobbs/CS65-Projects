# Ashlyn Hobbs
# ashlyn.hobbs@drake.edu
# November, 2022

# ---------------------------  subtask 1  ------------------------------
my_dict1 = {'a':'d', 'b':'e', 'c':'f'}
my_dict2 = {'A':'D', 'B':'E', 'C':'F'}


def concat_dictionary(my_dict1, my_dict2):
    
    return(my_dict1.update(my_dict2))

concat_dictionary(my_dict1, my_dict2)

print(my_dict1)

my_dict = {'a':'d', 'b':'e', 'c':'f'}

newDict = {}

def toggle_key_value_pair(my_dict):
    
    for k, v in my_dict.items():
        newDict[v] = k
        
    print(newDict)
    
toggle_key_value_pair(my_dict)
    

# ---------------------------  subtask 2  -------------------------------

# this function will create a dictionary with (key, value) mapping
    
def create_caesar_cipher_mapping(my_alphabet1, shift_amount):
    
    length = len(my_alphabet1)
    
    new_dictionary = {}
    
    for i in range(len(my_alphabet1)):
        index_mapped = (i+shift_amount) % length
        
        key   = my_alphabet1[i]
        value = my_alphabet1[index_mapped]
        
        new_dictionary.update({key:value})
        
    print("Alphabet in my_alphabet1 =", my_alphabet1)
    print("Caesar cipher mapping:")
    print("------------------------")
    print(new_dictionary)
    print("                                                   ")
    
    return new_dictionary


my_alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f']
shift_amount = int(input("Enter shift amount: "))
create_caesar_cipher_mapping(my_alphabet1, shift_amount)

# ----------------------------  subtask 3  ------------------------------

def encrypt_message(my_dict, my_string): 
    
    encrypted_message = ""
    
    for letter in my_string:
        if letter in my_dict:
            encrypted_message += my_dict[letter]
        else:
            encrypted_message += letter
    
    print(my_dict)
    print("Original message: ", my_string)
    print("---------------------------------------")
    print("Encrypted message: ", encrypted_message)
    print("---------------------------------------")
    
    encrypted_message2 = ""
    
    for letters in my_string:
        if letters in my_dict2:
            encrypted_message2 += my_dict2[letters]
        else:
            encrypted_message2 += letters
    
    print(my_dict2)
    print("Original message: ", my_string)
    print("---------------------------------------")
    print("Encrypted message: ", encrypted_message2)
    print("---------------------------------------")
    
    encrypted_message3 = ""
    
    for letter in my_string:
        if letter in my_alphabet:
            encrypted_message3 += my_alphabet[letter]
        else:
            encrypted_message3 += letter
    
    print(my_alphabet)
    print("Original message: ", my_string)
    print("---------------------------------------")
    print("Encrypted message: ", encrypted_message3)
    print("---------------------------------------")
    
    
    return encrypted_message, encrypted_message2, encrypted_message3
    
    
my_dict = {'a':'d', 'b':'e', 'c':'f', 'd':'a', 'e':'b', 'f':'c'}
my_dict2 = {'A':'D', 'B':'E', 'C':'F', 'D':'A', 'E':'B', 'F':'C'}

my_alphabet = {'a':'d', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'f':'i', 'g':'j', 'h':'k', 'i':'l', 'j':'m', 'k':'n', 'l':'o', 'm':'p', 'n':'q', 'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v', 't':'w', 'u':'x', 'v':'y', 'w':'z', 'x':'a', 'y':'b', 'z':'c'}

my_string = input("Original Message: ")

encrypt_message(my_dict, my_string)

# concat a dictionary

my_dict3 = {'a':'d', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'f':'i', 'g':'j', 'h':'k', 'i':'l', 'j':'m', 'k':'n', 'l':'o', 'm':'p', 'n':'q', 'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v', 't':'w', 'u':'x', 'v':'y', 'w':'z', 'x':'a', 'y':'b', 'z':'c'}
my_dict4 = {'A':'D', 'B':'E', 'C':'F', 'D':'G', 'E':'H', 'F':'I', 'G':'J', 'H':'K', 'I':'L', 'J':'M', 'K':'N', 'L':'O', 'M':'P', 'N':'Q', 'O':'R', 'P':'S', 'Q':'T', 'R':'U', 'S':'V', 'T':'W', 'U':'X', 'V':'Y', 'W':'Z', 'X':'A', 'Y':'B', 'Z':'C'}


def concat_dictionary(my_dict3, my_dict4):
    
    # making a "deep copy" of the original two dictionaries
    new_dict = {}
    
    for (k, v) in my_dict3.items():
        new_dict.update({k:v})
    
    for (k, v) in my_dict4.items():
        new_dict.update({k:v})
        
    return new_dict

my_dict5 = concat_dictionary(my_dict3, my_dict4)

print("my_dict3 = ", my_dict3)
print("                                                    ")
print("my_dict4 = ", my_dict4)
print("                                                    ")

print("Result of dictionary concatenation is my_dict5 = ", my_dict5)
print("                                                         ")
print("                                                         ")

# encrypt the new dictionary, my_dict5

encrypted_message4 = ""

for letter in my_string:
        if letter in my_dict5:
            encrypted_message4 += my_dict5[letter]
        else:
            encrypted_message4 += letter

print(my_dict5)
print("Original message: ", my_string)
print("---------------------------------")
print("                                  ")
print("Encrypted message5: ", encrypted_message4)