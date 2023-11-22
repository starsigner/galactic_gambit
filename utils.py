import os
from database import *

# initalize database 
c = connect_to_db()
create_user_table(c)

# clear terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# initalize stack for nav/return 
function_stack = []

# general input handling function
def get_input(prompt):
    user_input = input(prompt)
    if (user_input.lower() == '\x1b'):    
        popped_function = function_stack.pop()
        popped_function()
        return None 
    else:
        return user_input
    
def handle_none_input(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            return
        return result
    return wrapper

# star pattern 
def printStarPattern():
    print("☆⋆⭒⋆✵⋆★⋆☆⋆⭒⋆✵⋆★\n")