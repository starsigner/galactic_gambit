
import os
from database import *

# Clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initalize Database 
c = connect_to_db()
create_user_table(c)

# Main Menu
def mainMenu():
    print("\n")
    print("Games Table [0]\n")
    print("Help Desk [1]\n")
    print("Celestial Bar [2]\n")
    print("User Stats [3]\n")

# Landing Page
print("Welcome to the Galaxia Casino, located between exoplanet-544 and wormhole Venti!\n")
print("> Make an account (enter 0)\n")
print("> Login (enter 1)\n")
userLogin = input("")

# Create Account 
if (userLogin == "0"):
    username = input("What should we call you?")
    password = input('We have 3 other {}\'s who come to this casino, so better enter a password... \n Choose password: '.format(username))
    clear_screen()
    add_user(c, username, password)
    print("\nGreat! You've been entered into the galactic database. ['Yes' to continue]\n")
    print("You're all set {}. Head to the poker table, or grab some refreshments.".format(username))
    mainMenu()

# User Login 
if (userLogin == "1"):
    print("You're logging in, huh!")

