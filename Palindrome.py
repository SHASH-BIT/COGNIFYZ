def is_palindrome(value):
    
    text = str(value)
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    if text == reversed_text:
        return True
    else:
        return False
    
user_value = input("Enter a number or a string : ")

if is_palindrome(user_value):
    print(f"{user_value} is a palindrome! ")
else:
    print(f"{user_value} is not a palindrome.")    