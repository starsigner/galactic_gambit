from database import *
from constants import *

# def errorHandleUsername(username):
#    # duplicate username 
#    if user_exists(c, username):
#        print(DUPLICATE_USERNAME_ERROR)
#        createAccount()
#    # username validity
#    if len(username) < MIN_USERNAME_LEN:
#        print(MIN_USERNAME_ERROR)
#        createAccount()
#    if len(username) > MAX_USERNAME_LEN:
#        print(MAX_USERNAME_ERROR)
#        createAccount()

def has_symbol(password):
    
    for char in password:
        if char in SYMBOL_CHARACTERS_LIST:
            return True
        
    return False

def errorHandlePassword(password):
   # duplicate username check
   if len(password) < MIN_PASS_LEN:
       print(MIN_PASSWORD_ERROR)
       return True
   if (not has_symbol(password)):
       print(SPECIAL_CHAR_PASSWORD_ERROR)
       return True
   if any(char.isdigit() for char in password) == False:
       print(NUMERIC_CHAR_PASSWORD_ERROR)
       return True
   return False

