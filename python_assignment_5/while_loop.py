# while loop  use counter and user input validation
counter = 1

while counter <= 5:
    user_input = input("Enter a number between 1 and 10: ")
    
    if user_input.isdigit():
        number = int(user_input)
        
        if 1 <= number <= 10:
            print(f"You entered: {number}")
            counter += 1
        else:
            print("Please enter a number between 1 and 10.")
    else:
        print("Invalid input. Please enter a valid number.")
   