age = 23
name = "Baue"
fruit = {"mango", "banana", "orange", "apple"}

print(type(age))
print(type(name) == str)  # return true, if string
print(type(fruit))
print(isinstance(name, str))  # checking instance, if name == string => return true

# complex for complex number
# bool for booleans
# lists for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

# Arithmetic Operators
# +, -, *, /,
# %(reminder), 4 % 3 = 1
# ** (2 to the power 2) 4 ** 2 = 16
# //(flor - divide and gives an int by rounding) 5 // 2 = 2

age = 8
age += 8  # age = age + 8 = 16
age *= 8  # age = age * 8 = 64

# comparison operator
a = 1
b = 2

a == b  # False
a != b  # True
a > b  # False
a <= b  # True

# not, and, or operators
condition1 = True
condition2 = False

not condition1  # False
condition1 and condition2  # False
condition1 or condition2  # True

# OR operator
# or return the first value if true, if not then always the second value
print(0 or 1)  ## 1
print(False or "hey")  ## 'hey'
print("hi" or "hey")  ## 'hi
print([] or False)  ## 'False'
print(False or [])  ## '[]'


# And operator
# and only evaluates the second value if the first one is true
print(0 and 1)  ## 0
print(1 and 0)  ## 0
print(False and "hey")  ## False
print("hi" and "hey")  ## 'hey'
print([] and False)  ## []
print(False and [])  ## False

# # Bitwise Operators
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performes a binary NOT operaton
# << shift left operation
# >> shift right operation

# is # identity operator, compare 2 objects and return true or false
# in # membership operator, if value is contained in a list or in a sequence


# Ternary Operator
def is_adult(age):
    return True if age > 18 else False


name = "Nokib"
name += " is my name"
print(name)

print(
    """
    Hello!
    My name is Nokib.
    """
)


# isalpha() to check if a string contains only characters and is not empty
# isalnum() to check if a string contains characters or digits and is no empty
# isdecimal() to check if a string contains digits and is not empty
# lower() to get a lowercase version of a string
# islower() to check if a string is lowercase
# upper() to get a uppercase version of a string
# isupper() to check if a string is uppercase
# title() to get a capitalized version of a string
# startswith() to check if the string starts with a specific substring
# endswith() to check if the string ends with a specific substring
# replace() to replace a part of a string
# split() to split a string on a specific charecter separator
# strip() to trim the whitespace from a string
# join() to append new letters to a string 
# find() to find the position of a substring

print("bEAu person".title())
print("bEAu person".upper())
print("bEAu person".lower())
print("bEAu person".islower())
print("bEAu person".isupper())
