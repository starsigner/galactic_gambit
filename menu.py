from database import *
from constants import *
from utils import *

def printUserFile(username):
    print("{}'s FILE".format(username).upper())
    printStarPattern()
    print("Date Joined: {} \n".format(get_user_data(c, DATE_JOINED, username)))
    print("Lifetime Earnings: {} \n".format(get_user_data(c, LIFETIME_EARNINGS, username)))
    update_user_astrobucks(c, username, 4)
    print("Astrobucks: {} \n".format(get_user_data(c, ASTROBUCKS, username)))
    print("Level: ")
    print("DELETE ACCOUNT [0]")

def printRules():
    print("rules")

def printProfiles():
    print("profiles")

def printLevels():
    print("levels")

def printLore():
    print("lore")

def printHelpDesk():
    print(HELP_DESK_INTRO)
    print(HELP_OPTIONS)

    selectionOptions = {
        '0': printRules,
        '1': printProfiles,
        '2': printLevels,
        '3': printLore
    }

    userSelection = get_input("Select an option: ")
    function_stack.append(printHelpDesk)

    if userSelection in selectionOptions:
        selectionOptions[userSelection]()
        get_input("esc to return")
    else:
        print("Invalid option")

    