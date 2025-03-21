import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

email = input("📧 Enter email: ")
print("✅ Valid Email" if is_valid_email(email) else "❌ Invalid Email")
