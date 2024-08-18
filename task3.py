import re

def check_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Check strength
    if all([length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria]):
        return "Strong"
    elif length_criteria and any([lowercase_criteria, uppercase_criteria, number_criteria, special_char_criteria]):
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()




