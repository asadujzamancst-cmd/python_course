#return statements single value, multple value , list and dictionary return

#return single value

def add(a,b):
    sum = a+b
    return sum

result = add(30,4)
print(result)

#return multiple value
def multiple_return(a,b,c):
    sum = a+b
    dev=a-b-c
    mul=a*b*c
    return(sum,dev,mul)

result=multiple_return(3,4,5)
print(result)

#dictionary return
def dectionary_return(name,age):
    return{'name':name,'age':age}
result=dectionary_return('asad',21)
print(result)