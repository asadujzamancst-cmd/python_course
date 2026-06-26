# user_input_validation.py

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as e:
    print("Invalid input:", e)

else:
    print(f"Your age is {age}.")

finally:
    print("Program finished.")