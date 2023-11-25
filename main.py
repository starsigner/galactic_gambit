from stdiomask import getpass
from database import *
from constants import *
from utils import *
from menu import *
from validation import *
from datetime import datetime

# initialize current user 
current_username = None

@handle_none_input
def userFile():
    printUserFile(current_username)

def gamesTable():
    print("gamesTable")

def helpDesk():
    printHelpDesk()

def celestialBar():
    enterCelestialBar(current_username)

# Main Menu
@handle_none_input
def mainMenu():
    selectionOptions = {
        '0': gamesTable,
        '1': helpDesk,
        '2': celestialBar,
        '3': userFile
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

@handle_none_input
def createAccount():
        global current_username 
        username = get_input("What should we call you? ")
        errorHandleUsername(username)
        password = getpass('Welcome {}! Please enter a password to keep your account safe from Void Vandals. \n Choose password: '.format(username))
        while (errorHandlePassword(password)):
            password = getpass('Choose password: '.format(username))
        clear_screen()
        add_user(c, username, password, datetime.now().strftime('%Y-%m-%d'))
        current_username = username
        printStarPattern()
        print("\nGreat! You've been entered into the galactic database. ['Yes' to continue]\n")
        print("You're all set {}. Head to the poker table, or grab some refreshments.".format(username))
        mainMenu()

@handle_none_input
def login():
        global current_username

        loginUser = get_input("Username: ")
        loginPassword = getpass("Password: ")

        if check_credentials(c, loginUser, loginPassword):
            print(SUCCESSFUL_LOGIN)
            current_username = loginUser
        else:
            print(INCORRECT_LOGIN)
            login()
            
        mainMenu()

# Landing Page
@handle_none_input
def landing():
    print("\nWelcome to the Galactic Gambit, your local interstellar casino. To start playing, choose an option below:\n")
    printStarPattern()
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

