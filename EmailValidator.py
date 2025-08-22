
def valid_email(email):
    if"@" not in email:
        return False 
    
    parts = email.split("@")
    if len(parts) != 2:
        return False
    
    username , domain = parts 

    if not username:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    
    return True

user_email = input("Enter your email address : ")

if valid_email(user_email):
    print("Valid email address.")
else:
    print("Invalid email address.     " \
    "Please enter a valid email address")
