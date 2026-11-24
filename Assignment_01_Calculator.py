# Assignment 1: Calculator Program
# Supports basic and advanced arithmetic operations.

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        result = num1 + num2
    elif choice == "2":
        result = num1 - num2
    elif choice == "3":
        result = num1 * num2
    elif choice == "4":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        result = num1 / num2
    elif choice == "5":
        if num2 == 0:
            raise ZeroDivisionError("Modulus by zero is not allowed.")
        result = num1 % num2
    elif choice == "6":
        result = num1 ** num2
    else:
        raise ValueError("Please select a valid operation from 1 to 6.")

    print("Result:", result)

except ValueError as error:
    print("Invalid input:", error)
except ZeroDivisionError as error:
    print("Math error:", error)
