# Tuples
# Works same as Lists but You cannot modify the tuples # can't append, expand, remove....
names = ("Roger", "Syd")

names[0]  # Roger
names.index("Roger")  # 0

len(names)  # 2

# print("Roger" in names) # True
names[0:2]


# Dictionaries

dog = {"name": "Roger", "age": 8, "color": "green"}

dog["name"] = "Syd"

print(dog.get("name"))
print(
    dog.get("color", "brown")
)  # key and default value, if color doesn't exist then - brown if yes -then actual value, doesn't add the item to dict

print(dog["name"])

print(dog.pop("name"))
print(dog)

print("color" in dog)  # to check
print(dog.keys())  # to get all the keys
print(dog.values())  # to get all the values

print(list(dog.items()))  # will give each item of the dict in a list -- [('age', 8), ('color', 'green')]

print(len(dog)) # 3 -- length

dog["Favorite Food":] = "Meat" # To add a item

del dog["color"] # To delete a item from a dict

dogCopy = dog.copy() # To copy a dict
