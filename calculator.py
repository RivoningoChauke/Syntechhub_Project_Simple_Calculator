# SyntechHub Python Programming Internship
# Project 1: Simple Calculator
# This program performs basic arithmetic calculations through a command-line menu.


# Performs addition of two numbers
def add(a, b):
    return a + b


# Performs subtraction of two numbers
def subtract(a, b):
    return a - b


# Performs multiplication of two numbers
def multiply(a, b):
    return a * b


# Performs division and prevents division by zero
def divide(a, b):
    if b == 0:
        return None
    return a / b


# Selects the correct mathematical operation
# based on the operator provided by the user
def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return subtract(a, b)
    elif operator == "*":
        return multiply(a, b)
    elif operator == "/":
        return divide(a, b)
    else:
        return None


# Main function that controls the calculator menu
# and handles user interaction
def main():
    print("===== SYNTECHHUB SIMPLE CALCULATOR =====")

    # Keep the calculator running until the user chooses Exit
    while True:
        print("\nMenu:")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Choose an option: ")

        # Option 1 allows the user to perform a calculation
        if choice == "1":
            try:
                # Get the first number from the user
                first_number = float(input("Enter first number: "))

                # Get the mathematical operator
                operator = input("Enter operator (+, -, *, /): ")

                # Get the second number from the user
                second_number = float(input("Enter second number: "))

                # Check whether the user entered a valid operator
                if operator not in ["+", "-", "*", "/"]:
                    print("Invalid operator.")
                    continue

                # Prevent division by zero
                if operator == "/" and second_number == 0:
                    print("Error: Cannot divide by zero.")
                    continue

                # Perform the calculation
                result = calculate(
                    first_number,
                    operator,
                    second_number
                )

                # Display the result
                print(f"Result: {result}")

            # Handle invalid numerical input
            except ValueError:
                print("Invalid input. Please enter numbers correctly.")

        # Option 2 clears the current calculation
        elif choice == "2":
            print("\nCalculator cleared.")

        # Option 3 exits the calculator
        elif choice == "3":
            print("Thank you for using the calculator!")
            break

        # Handle an invalid menu selection
        else:
            print("Invalid menu option. Please choose 1, 2 or 3.")


# Start the calculator when this file is executed directly
if __name__ == "__main__":
    main()