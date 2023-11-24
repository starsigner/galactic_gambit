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

    