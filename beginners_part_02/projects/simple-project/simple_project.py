#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# We first import internal and external modules
# Then we import our own modules
from src.users import getUsersToCallToday
from src.today import getToday

# Then we declare constants.
API_USERS = "https://jsonplaceholder.typicode.com/users"


# Then we create the main function (the name is a convention).
def main():
    # We define docstrings in each function !!!
    """
    Main function of simple_project. Display the current date and the users to call.

    """
    print("Current date:", getToday())
    print("Users to call today:", getUsersToCallToday(API_USERS))


# This condition is True only if the script is called directly.
# It's false if we import the code in another script.
if __name__ == "__main__":
    main()
