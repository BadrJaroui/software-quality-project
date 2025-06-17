import re

def username_validation(username):
    #CHECK UNIQUENESS
    if len(username) < 8 or len(username) > 10:
        return False
    if not (isinstance(username[0], str)) or username[0] != "_":
        return False
    
    # check if contains only valid characters
    if not (re.match(r"^[a-zA-Z0-9_'.]+$", username)):
        return False
    
    else:
        return True
    
def username_to_lowercase(username):
    return username.lower()

    

def password_validation(password):
    if len(password) < 12 or len(password) > 30:
        return False
    
    # check if contains only valid characters
    if not re.fullmatch(r"^[a-zA-Z0-9~!@#$%&_\-+=`|\\(){}\[\]:;'<>,\.?\/]+$", password):
        return False
    
    # check if contains combination of atleast lowercase, uppercase, digit and special char
    has_lower = re.search(r"[a-z]", password)
    has_upper = re.search(r"[A-Z]", password)
    has_digit = re.search(r"\d", password)
    has_special = re.search(r"[~!@#$%&_\-+=`|\\(){}\[\]:;'<>,\.?\/]", password)
    if not (all([has_lower, has_upper, has_digit, has_special])):
        return False
    