import re

def pwd_strength(password):
    length = len(password) >= 8
    upper = re.search(r'[A-Z]', password) is not None
    lower = re.search(r'[a-z]', password) is not None
    digit = re.search(r'\d', password) is not None
    spcl_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    strength = sum([length, upper, lower, digit, spcl_char])
    
    if strength > 5:
        strength_level = "Excellent"
    elif strength == 5:
        strength_level = "Very Strong"
    elif strength == 4:
        strength_level = "Strong"
    elif strength == 3:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"
    
    feedback = []
    if not length:
        feedback.append("Password length should be at least 8 characters long.")
    if not upper:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit:
        feedback.append("Password should contain at least one digit.")
    if not spcl_char:
        feedback.append("Password should contain at least one special character.")
    return strength_level, feedback

password = input("Enter your password here: ")
strength, feedback = pwd_strength(password)
print(f"\nPassword strength:  {strength}")
if feedback:
    print("\nFeedback to improve password strength:")
    for suggestion in feedback:
        print(f"\t- {suggestion}")
    print("\n")