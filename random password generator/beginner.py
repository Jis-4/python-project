import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_numbers:
        characters += string.digits  # '0123456789'
    if use_symbols:
        characters += string.punctuation  # '!@#$%^&*()_+'

    # Generate password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User inputs
try:
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate password
    if not (use_letters or use_numbers or use_symbols):
        print("You must select at least one character type!")
    else:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")

except ValueError:
    print("Invalid input. Please enter a number for the password length.")
