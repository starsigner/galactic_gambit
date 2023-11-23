from database import *
from constants import *
from utils import *


def printUserStats(username):
    print("{}'s FILE".format(username).upper())
    printStarPattern()
    print("Date Joined: \n")
    print("Total Money Earned: \n")
    update_user_astrobucks(c, username, 4)
    print("Astrobucks: {} \n".format(get_user_astrobucks(c, username)))
    print("Level: ")

