
import os
from database import *

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# initalize database 
c = connect_to_db()
create_user_table(c)

# print star design pattern
def printStarDesign():
    print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")

def errorHandleUsername(username):
   print("test")
   # duplicate username?
   # invalid characters or length

# Main Menu
def mainMenu():
    print("Games Table [0]\n")
    print("Help Desk [1]\n")
    print("Celestial Bar [2]\n")
    print("User Stats [3]\n")

# Landing Page
print("\nWelcome to the Galactic Gambit, your local interstellar casino. To start playing, choose an option below:\n")
printStarDesign()
print("> Make an account (enter 0)\n")
print("> Login (enter 1)\n")
print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")
userLogin = input("")

# Create Account 
if (userLogin == "0"):
    username = input("What should we call you?")
    errorHandleUsername(username)
    password = input('We have 3 other {}\'s who come to this casino, so better enter a password... \n Choose password: '.format(username))
    clear_screen()
    add_user(c, username, password)
    printStarDesign()
    print("\nGreat! You've been entered into the galactic database. ['Yes' to continue]\n")
    print("You're all set {}. Head to the poker table, or grab some refreshments.".format(username))
    mainMenu()

# User Login 
if (userLogin == "1"):
    print("You're logging in, huh!")

