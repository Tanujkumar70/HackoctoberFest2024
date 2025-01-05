import re

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password is too short. Must be at least 8 characters."

    # Check for the presence of at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for the presence of at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for the presence of at least one digit
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    # Check for the presence of at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."

    return "Password is strong."

# Example usage
password = input("Enter a password to check: ")
result = check_password_strength(password)
print(result)
