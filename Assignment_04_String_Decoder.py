# Assignment 4: Secret Message Decoder

main_string = input("Enter the coded message: ")
substring = input("Enter the secret message (substring): ")

if main_string == substring:
    print("Strings are equal!")
elif substring in main_string:
    print("Substring found!")
else:
    print("Substring not found and strings are not equal.")
