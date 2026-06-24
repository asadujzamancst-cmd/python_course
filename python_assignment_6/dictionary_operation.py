#dictionary operation
my_dicti = {'a': 1, 
           'b': 2, 
           'c': 3}

#get 
get_b=my_dicti.get("b")
print(get_b)


#update

update_c =my_dicti.update({"c":"9"})
print(my_dicti)

#pop

pop_1 = my_dicti.pop("c")
print(my_dicti)
