# Assignment 5: Student Grade Calculator
# Each student takes five tests.

try:
    number_of_students = int(input("Enter the number of students: "))

    if number_of_students <= 0:
        raise ValueError("The number of students must be greater than zero.")

    class_total = 0

    for student_number in range(1, number_of_students + 1):
        print(f"\nEnter marks for Student {student_number}:")
        student_total = 0

        for test_number in range(1, 6):
            marks = float(input(f"Test {test_number} marks (0-100): "))

            if not 0 <= marks <= 100:
                raise ValueError("Marks must be between 0 and 100.")

            student_total += marks

        student_average = student_total / 5
        class_total += student_total
        print(f"Student {student_number} average: {student_average:.2f}")

    overall_average = class_total / (number_of_students * 5)
    print(f"\nOverall class average: {overall_average:.2f}")

except ValueError as error:
    print("Invalid input:", error)
