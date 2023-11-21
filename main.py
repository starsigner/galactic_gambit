
import os
from stdiomask import getpass
from database import *
from constants import *


# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# initalize database 
c = connect_to_db()
create_user_table(c)

# initalize stack for nav/return 
function_stack = []

# General input handling function
def get_input(prompt):
    user_input = input(prompt)
    if (user_input.lower() == '\x1b'):    
        popped_function = function_stack.pop()
        popped_function()
        return None 
    else:
        return user_input
    
def handle_none_input(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            return
        return result
    return wrapper

# star pattern 
def printStarDesign():
    print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")

# Main Menu
@handle_none_input
def mainMenu():
    print("Games Table [0]\n")
    print("Help Desk [1]\n")
    print("Celestial Bar [2]\n")
    print("User Stats [3]\n")
    function_stack.append(login)
   
def errorHandleUsername(username):
   # duplicate username 
   if user_exists(c, username):
       print(DUPLICATE_USERNAME_ERROR)
       createAccount()
   # username validity
   if len(username) < MIN_USERNAME_LEN:
       print(MIN_USERNAME_ERROR)
       createAccount()
   if len(username) > MAX_USERNAME_LEN:
       print(MAX_USERNAME_ERROR)
       createAccount()

def has_symbol(password):
    symbol_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"
    
    for char in password:
        if char in symbol_characters:
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

# Create Account 
@handle_none_input
def createAccount():
        username = get_input("What should we call you? ")
        errorHandleUsername(username)
        password = getpass('Welcome {}! Please enter a password to keep your account safe from Void Vandals. \n Choose password: '.format(username))
        while (errorHandlePassword(password)):
            password = getpass('Choose password: '.format(username))
        clear_screen()
        add_user(c, username, password)
        printStarDesign()
        print("\nGreat! You've been entered into the galactic database. ['Yes' to continue]\n")
        print("You're all set {}. Head to the poker table, or grab some refreshments.".format(username))
        function_stack.append(createAccount)
        mainMenu()

@handle_none_input
def login():
        loginUser = get_input("Username: ")
        loginPassword = getpass("Password: ")
        function_stack.append(login)
        if check_credentials(c, loginUser, loginPassword):
            print(SUCCESSFUL_LOGIN)
        else:
            print(INCORRECT_LOGIN)
            login()

# Landing Page
def landing():
    print("\nWelcome to the Galactic Gambit, your local interstellar casino. To start playing, choose an option below:\n")
    printStarDesign()
    print("> Make an account (enter 0)\n")
    print("> Login (enter 1)\n")
    print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")
    userLogin = input("")
    function_stack.append(landing)
    if (userLogin == "0"):
        createAccount()
    else:
        login()

landing()

