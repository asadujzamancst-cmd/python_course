# Nested If Statements in Python
marks = 85

if marks >= 0:
    print("Valid marks")
    if marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Invalid marks")