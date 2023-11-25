from database import *
from constants import *
from utils import *
import random

def printUserFile(username):
    print("{}'s FILE".format(username).upper())
    printStarPattern()
    print("Date Joined: {} \n".format(get_user_data(c, DATE_JOINED, username)))
    print("Lifetime Earnings: {} \n".format(get_user_data(c, LIFETIME_EARNINGS, username)))
    update_user_astrobucks(c, username, 4)
    print("Astrobucks: {} \n".format(get_user_data(c, ASTROBUCKS, username)))
    print("Level: ")
    print("Awards won: ")
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
        keyboard_count += 1
    # function_stack.append(enterCelestialBar(username))
    chosen_drink = get_input("What will you be having tonight?")
    chosenDrinkEffects(CELESTIAL_BAR_MENU_OPTIONS[random_drinks[int(chosen_drink)]])

@handle_none_input
def chosenDrinkEffects(drink):
    print(drink)
