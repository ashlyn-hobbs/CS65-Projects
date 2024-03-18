# Author's name: Ashlyn Hobbs
# Author's contact: ashlyn.hobbs@drake.edu
# Date: (September 13, 2022)
# Collaborator:
#   No Partner

#________________________  Task 1  _________________________________
# a brief description of your solution or motivation behind your logic

#this user defined function adds two numbers
def add_numbers(num1, num2):
    res1 = num1 + num2
    return res1

a = 10
b = 4
res = add_numbers(a, b)
print("add function: invoked with a =", a, ", b =", b, " and result =", res)

#this user defined function subtracts second number from the first
def sub_numbers(num1, num2):
    res2 = num1 - num2
    return res2

c = 27
d = 9
res = sub_numbers(c, d)
print("sub function: invoked with c =", c, ", d =", d, " and result =", res)

#this user defined function multiplies two numbers
def mul_numbers(a, b):
    res3 = a * b
    return res3

e = 13
f = 6
res = mul_numbers(e, f)
print("mul function: invoked with e =", e, ", f =", f, " and result =", res)

#this user defined function dvides the first number by the first 
def div_numbers(num1, num2):
    res4 = num1 // num2
    return res4

g = 96
h = 12
res = div_numbers(96,12)
print("div function: invoked with g =", g, ", h =", h, " and result =", res)