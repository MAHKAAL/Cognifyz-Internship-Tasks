import re

def validate_email(email):
    email_pattern = re.compile(
        r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if email_pattern.match(email):
        return ("is a valid email address.")
    else:
        return ("is an invalid email address.")

email = input("Enter your email here: ")
print(f"{email} {validate_email(email)}")