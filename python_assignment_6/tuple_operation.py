#tuple operation count
my_tuple = (1, 2, 3, 4, 5, 2, 3)
#count
count_of_2 = my_tuple.count(2)
print("Count of 2 in tuple:", count_of_2)

#index
index_of_3 = my_tuple.index(3)
print("Index of 3 in tuple:", index_of_3)

#tuple slicing
sliced_tuple = my_tuple[1:5]
print("Sliced tuple:", sliced_tuple)

#tuple list conversion
tuple_1 = (1, 2, 3, 4, 5)
converted_list = list(tuple_1)
converted_list.append(6)
tuple_2 = tuple(converted_list)
print(tuple_2)