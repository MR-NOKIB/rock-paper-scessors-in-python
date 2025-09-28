# Sets
# No repeat item, will return one of each item
set1 = {"Roger", "Syd", "Kal"}
set2 = {"Roger"}
set3 = {"Kill", "Luna", "Roger"}

intersect = set1 & set2 # Will return common items between sets in a set -- {'Roger'}
print(intersect)

mod = set1 | set3 # Will return all the items between two sets - common items will no repeat - just one
print(mod)

difference = set1 - set2 # Will return Uncommon items between two sets - {'Syd'}
print(difference)

one = set1 > set2 # If set1 has all the item that set2 has - True
two = set1 < set2 # If set2 has all the item that set1 have - False

print(list(set1)) # Will return a list with all the items of the set
print(len(set1)) # Length
