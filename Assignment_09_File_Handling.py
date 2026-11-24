# Assignment 9: File Reading Program

filename = input("Enter the name of the text file (for example, sample.txt): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        contents = file.read()

    print("\nFile contents:")
    print(contents)

except FileNotFoundError:
    print("Error: The file was not found. Check its name and location.")
except PermissionError:
    print("Error: You do not have permission to read this file.")
except OSError as error:
    print("File error:", error)
