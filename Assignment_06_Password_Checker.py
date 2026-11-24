# Assignment 6: Password Strength Checker
# Type "stop" to exit.

while True:
    password = input("\nEnter a password (or type stop to exit): ")

    if password.lower() == "stop":
        print("Exiting the password checker.")
        break

    has_uppercase = any(character.isupper() for character in password)
    has_lowercase = any(character.islower() for character in password)
    has_digit = any(character.isdigit() for character in password)

    if (len(password) >= 8 and has_uppercase
            and has_lowercase and has_digit):
        print("Strong password.")
    else:
        print("Weak password.")
