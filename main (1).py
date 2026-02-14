import re

def check_password(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        print("Password is too short. Minimum 8 characters required.")
    if digit_error:
        print("Password must contain at least one number.")
    if uppercase_error:
        print("Password must contain at least one uppercase letter.")
    if lowercase_error:
        print("Password must contain at least one lowercase letter.")
    if symbol_error:
        print("Password must contain at least one special character.")

    if not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error):
        print("Password is very strong!")

if __name__ == "__main__":
    pwd = input("Enter your password to check its strength: ")
    check_password(pwd)