#text file creat , read ,write ,renamew ,dellete

#crete file 
with open ('new_2.txt','w') as file:
    file.write('hi,')


#read file

with open('new.txt','r') as file:
    content = file.read()
    print(content)



    #write file

with open ('new_2.txt','w') as file:
    file.write('new text')


    #renaming 

    import os 
    os.rename('new.txt','new_1.txt')


#deleting
#import os
os.remove('new_3.txt')