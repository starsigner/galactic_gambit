
import os
from stdiomask import getpass
from database import *

# constants
MIN_USERNAME_LEN = 1
MAX_USERNAME_LEN = 20

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# initalize database 
c = connect_to_db()
create_user_table(c)

clear_database(c)

# print star design pattern
def printStarDesign():
    print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")

# Main Menu
def mainMenu():
    print("Games Table [0]\n")
    print("Help Desk [1]\n")
    print("Celestial Bar [2]\n")
    print("User Stats [3]\n")
   
def errorHandleUsername(username):
   # duplicate username check
   if user_exists(c, username):
       print("That username already exists. Please try again.")
       createAccount()
   # username validity
   if len(username) < MIN_USERNAME_LEN:
       print("Username must be at least 1 character.")
       createAccount()
   if len(username) > MAX_USERNAME_LEN:
       print("Please keep your username under 20 character.")
       createAccount()

# Create Account 
def createAccount():
    if (userLogin == "0"):
        username = input("What should we call you? ")
        errorHandleUsername(username)
        password = getpass('Welcome {}! Please enter a password to keep your account safe from Void Vandals. \n Choose password: '.format(username))
        clear_screen()
        add_user(c, username, password)
        printStarDesign()
        print("\nGreat! You've been entered into the galactic database. ['Yes' to continue]\n")
        print("You're all set {}. Head to the poker table, or grab some refreshments.".format(username))
        mainMenu()


# Landing Page
print("\nWelcome to the Galactic Gambit, your local interstellar casino. To start playing, choose an option below:\n")
printStarDesign()
print("> Make an account (enter 0)\n")
print("> Login (enter 1)\n")
print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")
userLogin = input("")
createAccount()


# User Login 
if (userLogin == "1"):
    print("You're logging in, huh!")

