# for loop 

name = "asadujzaman "
for char in name:
    print(char)

    #FOR LOOP WITH RANGE FUNCTION
say = "i love python"

for i in range(5):
    print(say)

# for loop with range function and step value
for i in range(0, 10, 2):
    print(i)

#for loop with break statement
for i in range(10):
    if i == 5:
        break
    print(i)

    #for loop with  continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)