# Assignment 3: Assignment List Manager

assignments = [
    "Python Assignment",
    "Data Structures Assignment",
    "Mathematics Assignment"
]

print("Current assignments:")
for task in assignments:
    print("-", task)

new_assignment = input("\nEnter a new assignment to add: ").strip()
if new_assignment:
    assignments.append(new_assignment)
    print("Assignment added.")

completed = input("Enter the completed assignment to remove: ").strip()
if completed in assignments:
    assignments.remove(completed)
    print("Completed assignment removed.")
else:
    print("That assignment was not found in the list.")

print("\nUpdated assignment list:")
if assignments:
    for task in assignments:
        print("-", task)
else:
    print("No pending assignments.")
