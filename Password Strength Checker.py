import string

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Conditions
    if len(password) >= 8:
        strength += 1
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    # Strength based on score
    if strength == 5:
        remarks = "Excellent password!"
    elif strength == 4:
        remarks = "Strong password."
    elif strength == 3:
        remarks = "Medium strength. Improve it."
    elif strength == 2:
        remarks = "Weak password!"
    else:
        remarks = "Very weak password!"

    return remarks


password = input("Enter a password: ")
print(check_password_strength(password))
