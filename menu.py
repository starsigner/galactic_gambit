from database import *
from constants import *
from utils import *
import random

# USER PROFILE  
# prints the user's profile with date joined, lifetime earnings, astrobucks, awards won, and current level
def printUserFile(username):
    print("{}'s FILE".format(username).upper())
    printStarPattern()
    print("Date Joined: {} \n".format(get_user_data(c, DATE_JOINED, username)))
    print("Lifetime Earnings: {} \n".format(get_user_data(c, LIFETIME_EARNINGS, username)))
    update_user_astrobucks(c, username, 4)
    print("Astrobucks: {} \n".format(get_user_data(c, ASTROBUCKS, username)))
    print("Awards won: ")
    print("DELETE ACCOUNT [0]")

# HELP DESK 

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

# CELESTIAL BAR 

def getRandomDrinks():
    drink_len = len(CELESTIAL_BAR_MENU_OPTIONS)
    rand_drinks = random.sample(range(drink_len), 4)
    return rand_drinks 

@handle_none_input
def enterCelestialBar(username):
    print("CELESTIAL BAR\n")
    print("Astrobucks: {} \n".format(get_user_data(c, ASTROBUCKS, username)))
    printStarPattern()
    keyboard_count = 0
    random_drinks = getRandomDrinks()
    for num in random_drinks:
        keyboard_count_str = str(keyboard_count)
        drink_name, drink_price = CELESTIAL_BAR_MENU_OPTIONS[num]
        print(f"{drink_name}: {drink_price} AB [{keyboard_count_str}]")
        print("\n")
        keyboard_count += 1
    function_stack.append(enterCelestialBar)
    chosen_drink = get_input("What will you be having tonight?")
    buyDrink(CELESTIAL_BAR_MENU_OPTIONS[random_drinks[int(chosen_drink)]], username)

@handle_none_input
def buyDrink(drink, username):
    update_user_astrobucks(c, username, 500)
    curr_astrobucks = get_user_data(c, ASTROBUCKS, username)
    drink_price = drink[1]
    if (curr_astrobucks < drink_price):
        print("NOT ENOUGH FUNDS")
    else:
        print("DRINKING")
        update_user_astrobucks(c, username, curr_astrobucks - drink_price)
        print(get_user_data(c, ASTROBUCKS, username))
    get_input("esc to return")

def games_table(username):
    print("games table")





