# try else finally
devide= int(input('enter a number '))
try :
    content = 10/devide

except ZeroDivisionError:
    print('can not divided by o ')

else :

    print('enter integer number: ')

finally:
    print (f'the result is : {content}')