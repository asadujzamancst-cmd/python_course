#list operation
my_list = [1, 2, 3, 4, 5]
#append
my_list.append(6)
print("After append:", my_list)

#insert
my_list.insert(2, 10)
print("After insert:", my_list)

#extend
my_list.extend([7, 8, 9])
print("After extend:", my_list)

#remove
my_list.remove(3)
print("After remove:", my_list)

#pop
popped_element = my_list.pop()
print("After pop:", my_list)


#sort
my_list.sort()
print("After sort:", my_list)

#reverse
my_list.reverse()
print("After reverse:", my_list)

# list slicing
sliced_list = my_list[1:5]
print("Sliced list:", sliced_list)

