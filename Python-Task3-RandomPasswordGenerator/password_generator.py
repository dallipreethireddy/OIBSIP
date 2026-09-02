import random
import string

print("===================================")
print("     RANDOM PASSWORD GENERATOR")
print("===================================")

while True:

    # Get password length
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    # Display character type options
    print("\nChoose character types to include:")
    print("1. Uppercase letters (A-Z)")
    print("2. Lowercase letters (a-z)")
    print("3. Numbers (0-9)")
    print("4. Symbols (!@#$...)")

    choice = input("Enter your choices (example: 1,2,3,4): ")

    # Convert choices into a list
    choices = [x.strip() for x in choice.split(",")]

    # Validate choices
    valid_choices = {"1", "2", "3", "4"}

    if not choices or not all(x in valid_choices for x in choices):
        print("Error: Please select only 1, 2, 3, or 4.")
        continue

    # Remove duplicate choices
    choices = list(set(choices))

    # At least 2 character types
    if len(choices) < 2:
        print("Error: Please select at least 2 character types.")
        continue

    # Create character pool
    characters = ""

    if "1" in choices:
        characters += string.ascii_uppercase

    if "2" in choices:
        characters += string.ascii_lowercase

    if "3" in choices:
        characters += string.digits

    if "4" in choices:
        characters += string.punctuation

    # Generate password
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\n-----------------------------------")
    print("Generated Password:", password)
    print("-----------------------------------")

    # Generate another password
    again = input("\nGenerate another password? (Y/N): ")

    if again.lower() != "y":
        print("\nThank you for using Random Password Generator!")
        break
