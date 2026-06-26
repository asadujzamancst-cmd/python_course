try:
    with open('my_name.txt') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print('File not found')

except ValueError:
    print('Value Error occurred')

except ZeroDivisionError:
    print('Cannot divide by zero')