name = "Nokib is cool"

print("nok'ib")
print("nok\"ib") # \ means skip character
print('nok"ib')
print("no\nkib") # \n means new line -no in first line and kib in second line

print(name[0]) # will return n, index starts from 0, 1,   from ending -1, -3

print(name[1:4]) # will return specific substring, from index 1 to 3 - oki
print(name[:8]) # nokib is

def get_ans(value):
    return "hello" if value == 1 else "gelo"

print(get_ans(1))

ingredients_purchased = True
meal_cooked = False

ready_to_serve = any([ingredients_purchased, meal_cooked]) # either of the value is True # True
ready_to_serve = all([ingredients_purchased, meal_cooked]) # all of the value is True # False


# Number
n1 = 12 # INT
n2 = 2.1 # FLOAT

num1 = 2 + 3j # complex j
num2 = complex(2,3) # 2 is real part, and 3 in imaginary part
print(num1.real, num2.imag)


abs(-5.5) # 5.5 # will return absolute value, every num in positive
round(5.49) # 5 # round to the nearest integer
round(5.49, 1) # 5.5  # round to 1 decimal point

