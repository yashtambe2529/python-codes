# Assignment 7: Daily Calorie Calculator

def calculate_calories(carbs, fats, proteins):
    """Calculate calories from carbohydrates, fats, and proteins."""
    return (carbs * 4) + (fats * 9) + (proteins * 4)


try:
    carbs = float(input("Enter carbohydrates consumed (grams): "))
    fats = float(input("Enter fats consumed (grams): "))
    proteins = float(input("Enter proteins consumed (grams): "))

    if min(carbs, fats, proteins) < 0:
        raise ValueError("Nutrient amounts cannot be negative.")

    total_calories = calculate_calories(carbs, fats, proteins)
    print(f"Total daily caloric intake: {total_calories:.2f} calories")

except ValueError as error:
    print("Invalid input:", error)
