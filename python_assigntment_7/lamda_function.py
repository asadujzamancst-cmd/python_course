#lamda , map(),filter(),sorted()

#lamda function

add = lambda:9+8
print(add)

#using map fucntion

numbers =[1,2,9,3,5,4,6,8]
result = map(lambda x: x**2,numbers)
print(list(result))


#using filter
filter_num = filter(lambda x:x<5 and x%2==0,numbers)
print(list(filter_num))

#using sorted()
sorted_use = sorted(numbers,key=lambda x : x%10)
print(sorted_use)