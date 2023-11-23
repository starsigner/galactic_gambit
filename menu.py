from database import *
from constants import *
from utils import *


def printUserStats(username):
    update_user_astrobucks(c, username, 4)
    print(get_user_astrobucks(c, username))

