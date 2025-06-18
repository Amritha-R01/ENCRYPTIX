import random
import string

print("=== Password Generator ===")

try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        print("Password length must be positive.")
    else:
        use_uppercase = input("Include uppercase letters? (y/n): ").lower()
        use_lowercase = input("Include lowercase letters? (y/n): ").lower()
        use_digits = input("Include digits? (y/n): ").lower()
        use_symbols = input("Include symbols? (y/n): ").lower()

        while True:
            characters = ""
            if use_uppercase == "y":
                characters += string.ascii_uppercase
            if use_lowercase == "y":
                characters += string.ascii_lowercase
            if use_digits == "y":
                characters += string.digits
            if use_symbols == "y":
                characters += string.punctuation

            if not characters:
                print("Error: You must select at least one character type.")
                break

            password = ''.join(random.choice(characters) for _ in range(length))
            print("\nGenerated Password:", password)

            gen = input("Regenerate password? (y/n): ").lower()
            if gen != "y":
                print("Thank you!")
                break
except ValueError:
    print("Please enter a valid number.")
