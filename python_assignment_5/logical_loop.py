# logical operators and or not

x = 5
y = 10
z = 15
#and operator
if x < y and y < z:
    print("Both conditions are true.")

#or operator
if x < y or y > z:
    print("At least one condition is true.")

#not operator
if not (x > y):
    print("The condition is false.")