# Assignment 2: Earth and Moon Weight Calculator
# The manual refers to an external "Q01 challenge 1" file that was
# not included, so this is a complete implementation of the stated task.

EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.62


def calculate_weight(mass, gravity):
    """Return weight in newtons."""
    return mass * gravity


try:
    mass = float(input("Enter the mass of the object in kg: "))

    if mass < 0:
        print("Mass cannot be negative.")
    else:
        earth_weight = calculate_weight(mass, EARTH_GRAVITY)
        moon_weight = calculate_weight(mass, MOON_GRAVITY)

        print(f"Weight on Earth: {earth_weight:.2f} N")
        print(f"Weight on Moon: {moon_weight:.2f} N")

except ValueError:
    print("Please enter a valid numerical mass.")
