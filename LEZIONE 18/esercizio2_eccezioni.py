'''Password Validation:  Write a function validate_password(password) that checks whether a password meets the following criteria: Minimum length of 20 characters, At least three uppercase letters, At least four special characters (non-alphanumeric). If the password is valid, the function should return True. If the password is invalid, the function should raise a built-in exception (e.g., ValueError) with a message indicating which criteria were not met.'''


from typing import Any

def validate_password(password:any)->None:
    cont_upper = 0
    cont_special = 0
    for char in password:
        if char.isupper():
            cont_upper += 1
        if not char.isalnum():
            cont_special += 1
    
    if cont_upper < 3:
        raise ValueError ("The password must have three upppercase characters")
    if cont_special < 4:
        raise ValueError("The password must have at least four special characters")
    if len(password)< 20:
        raise ValueError("The password must be at least 20 characters long")
    
    return print("Password is valid")
    
    


validate_password("AbcdeFgHiLmnPqrsssdsdsd!!!")





