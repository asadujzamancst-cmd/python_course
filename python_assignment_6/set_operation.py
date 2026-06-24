#set operations

my_set = {1, 2, 3, 4, 5}
#add
my_set.add(6)
print("After add:", my_set)

#remove
my_set.remove(3)
print("After remove:", my_set)

#union
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

#intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

#difference
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)

