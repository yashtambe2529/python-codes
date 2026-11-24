# Assignment 8: Area of Different Shapes
# A single function handles different shapes based on its arguments.

import math


def calculate_area(shape, *dimensions):
    """Calculate area for a circle, rectangle, or triangle."""
    shape = shape.lower()

    if shape == "circle" and len(dimensions) == 1:
        radius = dimensions[0]
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return math.pi * radius ** 2

    if shape == "rectangle" and len(dimensions) == 2:
        length, width = dimensions
        if length < 0 or width < 0:
            raise ValueError("Dimensions cannot be negative.")
        return length * width

    if shape == "triangle" and len(dimensions) == 2:
        base, height = dimensions
        if base < 0 or height < 0:
            raise ValueError("Dimensions cannot be negative.")
        return 0.5 * base * height

    raise ValueError("Invalid shape or incorrect number of dimensions.")


print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

try:
    choice = input("Choose a shape (1-3): ").strip()

    if choice == "1":
        radius = float(input("Enter radius: "))
        area = calculate_area("circle", radius)
    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = calculate_area("rectangle", length, width)
    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = calculate_area("triangle", base, height)
    else:
        raise ValueError("Please choose 1, 2, or 3.")

    print(f"Area: {area:.2f}")

except ValueError as error:
    print("Invalid input:", error)
