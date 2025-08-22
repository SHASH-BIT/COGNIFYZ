import re 

def password_strength_checker(password):

    length_error = len(password) < 8 
    uppercase_error = re.search(r"[A-Z]",password) is None
    lowercase_error = re.search(r"[a-z]",password) is None
    digit_error = re.search(r"\d",password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\:;{}|<>]",password) is None

    errors = []
    if length_error:
        errors.append("Password must be atleast 8 characters long. ")
    if uppercase_error:
        errors.append("Password must contain atleast one uppercase letter. ")
    if lowercase_error:
        errors.append("Password must contain atleast one lowercase letter. ")
    if digit_error:
        errors.append("Password must contain atleast one digit. ")
    if special_char_error:
        errors.append("Password must contain atleast one special character. ")
    
    if not errors:
        return " STRONG PASSWORD "
    else:
        return"\n".join(errors)

user_password = input("Enter a password to check whether it is strong or weak password : ")
print(password_strength_checker(user_password))