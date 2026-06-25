#args and kwargs 

#args * symbol diya tuple 

def names(*name):
    for i in (name):
        print(str(i))

names('asad','uj','zaman')


#kwargs ** symbol  dictionary 

def names_2(**name_3):
    for key,value in name_3.items():
        print(f'{key}:{value}')
names_2(name='asd', age='21', city='rajshahi')