#!/usr/bin/python3
def validate_password(password):
    if (len(password) >= 8):
        uppercase = False
        lowercase = False
        digit = False
        space = True

        for char in password:
            if (char.isupper()):
                uppercase = True
            if (char.islower()):
                lowercase = True
            if (char.isdigit()):
                digit = True
            if (char == " "):
                space = False
        return uppercase and lowercase and digit and space
    else:
        return False