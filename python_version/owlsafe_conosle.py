import os
import random
import hashlib

CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_+="
PASSWORD_LENGTH = 12
PASSWORD_FILE = "storage/password.txt"
HASH_FILE = "storage/db.txt"

def generate_random_password(length=PASSWORD_LENGTH):
    return "".join(random.choice(CHARACTERS) for _ in range(length))

def validate_input(identifier):
    invalid_chars = "/\\:*?\"<>|"

    if any(char in identifier for char in invalid_chars):
        raise ValueError("Identifier contains invalid characters")
    
    return identifier.strip()

def save_password(identifier, password, hashed_password):
    try:
        with open(PASSWORD_FILE, 'a') as file:
            file.write(f"{identifier}\n{password}\n")

        with open(HASH_FILE, 'a') as file:
            file.write(f"{hashed_password}\n")

        print(f"Password saved to '{PASSWORD_FILE}'.")

    except IOError as e:
        print(f"File error: {e}")

def main():
    try:
        # Creates the files where the password and hashed passwords are going to be stored
        if not os.path.exists(PASSWORD_FILE):
            open(PASSWORD_FILE, 'w').close()
        if not os.path.exists(HASH_FILE):
            open(HASH_FILE, 'w').close()

        print("Welcome to the Owl Safe!")
        
        while True:
            print("\nChoose an option:")
            print("1. Generate a new password")
            print("2. Retrieve a password")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                os.system('cls')
                identifier = validate_input(input("Enter a name for this password: "))
                with open(PASSWORD_FILE, 'r') as file:
                    lines = file.readlines()

                identifier_exists = False
                # Checks in the password file if the identifier exists to prevent duplicates.
                for line in lines:
                    if identifier in line.strip():
                        identifier_exists = True
                        break
                
                if identifier_exists:
                    print("Identifier already exists.")
                else:
                    password = generate_random_password()
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                        
                    save_password(identifier, password, hashed_password)
                    print(f"Password Generated!")

            elif choice == '2':
                os.system('cls')
                identifier = validate_input(input("Enter the name for the password you are searching for: "))
                with open(PASSWORD_FILE, 'r') as file:
                    lines = file.readlines()
                    # Runs a for loop with i to count the index number untill it finds the identifier then goes one line down to get the password
                    for i, line in enumerate(lines):
                        if identifier in line:
                            if i + 1 < len(lines):
                                password = lines[i + 1].strip()
                                print(f"The password under the name {identifier} is: {password}")
                                break
                    else:
                        print("Identifier not found.")
                        continue
            elif choice == '3':
                os.system('cls')
                print("Goodbye!")
                break
            
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
