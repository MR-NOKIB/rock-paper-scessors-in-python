dogs = ["Roger", 1, "Syd", True, "Quincy", 7]

print("Beau" in dogs)  # False

dogs[2] = "Beau"  # Will replace the 2nd index with Beau
print(dogs[2:4])  # will slice the lists # ['Beau', True]
print(dogs[:3])
print(dogs[3:])

print(len(dogs))

dogs.append("Judah")  # Adding an item to a list
dogs.extend(["Cat", 5])  # Adding multiple items to a list
dogs += ["Kala", 8]  # Same as extend
dogs.remove("Quincy")  # Will remove Quincy from the list
dogs.pop()  # Will remove the last item from the list and return the list
dogs.insert(2, "Test")  # to add a item at a specific index
dogs[1:1] = ["Test1", "Test2"]  # to add multiple items at a specific index

# Sort()
# Sort modify the original list contents orders

items = ["Pen", "Book", "Laptop", "Pencil", "Mouse", "Light"]
items.sort()  # Will sort all the items in alphabetical order # Sort as uppercase first
items.sort(key=str.lower)

itemsCopy = items[:]

# Sorted()
print(sorted(items, key=str.lower)) # sort in a new list without modifying the original list
