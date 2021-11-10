# Calculator Program Using Class

# Create a class Calculator and define all the functions

class Calculator:
    def addition(self):
        print(a + b)

    def subtraction(self):
        print(a - b)

    def multiplication(self):
        print(a * b)

    def division(self):
        print(a / b)


# Take inputs from the user and create an object

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Calculator()

# create choices for the user to perform which operation they need and print out the solution

choice = 1
while choice != 0:

    print("1. ADDITION")

    print("2. SUBTRACTION")

    print("3. MULTIPLICATION")

    print("4. DIVISION")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(obj.addition())

    elif choice == 2:
        print(obj.subtraction())

    elif choice == 3:
        print(obj.multiplication())

    elif choice == 4:
        print(obj.division())

    else:
        print("Invalid choice")
