# general_exception.py

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except Exception as e:
    print("An error occurred:", e)

finally:
    print("Program finished.")