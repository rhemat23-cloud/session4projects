import os
import json
import getpass
# File to store user credentials
USER_FILE = "users.json"

# Load existing users from file
def load_users():
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

# Save users to file
def save_users(users):
    try:
        with open(USER_FILE, "w") as f:
            json.dump(users, f)
    except IOError:
        print("Error: Could not save user data.")

# Validate username and password rules
def validate_credentials(username, password):
    if not username or not password:
        return False, "Username and password cannot be empty."
    if len(username) < 3:
        return False, "Username must be at least 3 characters."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    return True, ""

# Register a new user
def register(users):
    username = input("Enter new username: ").strip()
    password = getpass.getpass("Enter new password: ").strip()

    valid, msg = validate_credentials(username, password)
    if not valid:
        print(f"Error: {msg}")
        return users

    if username in users:
        print("Error: Username already exists.")
        return users

    users[username] = password
    save_users(users)
    print("Registration successful!")
    return users

# Login existing user
def login(users):
    username = input("Enter username: ").strip()
    password = getpass.getpass("Enter password: ").strip()

    if username in users and users[username] == password:
        print(f"Welcome, {username}! Login successful.")
    else:
        print("Invalid username or password.")

# Main menu
def main():
    users = load_users()

    while True:
        print("\n--- User Login System ---")
        print("1. Register")
        print("2. Login")
        print("3.exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            users = register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":

            print("thank you visiting us")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
