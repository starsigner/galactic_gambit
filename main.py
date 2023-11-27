from stdiomask import getpass
from database import *
from constants import *
from utils import *
from menu import *
from validation import *
from datetime import datetime

current_logged_in_username = None 

# function that welcomes the user and prompts for sign up or login
def landing():

    print("\nWelcome to the GALACTIC GAMBIT, your local interstellar casino. To start playing, choose an option below:\n")
    printStarPattern()
    print("> Make an account [0]\n") 
    print("> Login [1]\n")
    printStarPattern()
    userLogin = input("")
    clear_screen()
    function_stack.append(landing)

    if (not int(userLogin)):
        createAccount()
    else:
        login()

# function to create an account for the user
def createAccount():
        print("LET'S GET YOU SET UP. Follow the instructions below.\n")
        printStarPattern()
        global current_logged_in_username 
        username = get_input("What should we call you? ")
        errorHandleUsername(username)
        password = getpass('Welcome {}! Please enter a password to keep your account safe from Void Vandals. \nChoose password: '.format(username))
        while (errorHandlePassword(password)):
            password = getpass('Choose password: '.format(username))
        clear_screen()
        add_user(c, username, password, datetime.now().strftime('%Y-%m-%d'))
        current_logged_in_username = username
        printStarPattern()
        print("\nGreat! You've been entered into the galactic database.\n")
        print("You're all set {}. Head to the poker table, or grab some refreshments.".format(username))
        mainMenu()

# function that allows the user to login
def login():
        global current_logged_in_username

        loginUser = get_input("Username: ")
        loginPassword = getpass("Password: ")

        if check_credentials(c, loginUser, loginPassword):
            print(SUCCESSFUL_LOGIN)
            current_logged_in_username = loginUser
        else:
            print(INCORRECT_LOGIN)
            login()
            
        mainMenu()

# function that checks username for validity 
def errorHandleUsername(username):
   if user_exists(c, username):
       print(DUPLICATE_USERNAME_ERROR)
       createAccount()
   if len(username) < MIN_USERNAME_LEN:
       print(MIN_USERNAME_ERROR)
       createAccount()
   if len(username) > MAX_USERNAME_LEN:
       print(MAX_USERNAME_ERROR)
       createAccount()

def mainMenu():

    selectionOptions = {
        '0': lambda: games_table(current_logged_in_username),
        '1': printHelpDesk,
        '2': lambda: enterCelestialBar(current_logged_in_username),
        '3': lambda: printUserFile(current_logged_in_username)
    }

    print("Games Table [0]\n")
    print("Help Desk [1]\n")
    print("Celestial Bar [2]\n")
    print("User File [3]\n")

    userSelection = get_input("Select an option: ")
    function_stack.append(mainMenu)

    if userSelection in selectionOptions:
        selectionOptions[userSelection]()
        get_input("esc to return")
    else:
        print("Invalid option")

# starting point of the Galactic Gambit application.
# initiates the landing function, which displays the welcome page and prompts the user to sign up or log in.
landing()

