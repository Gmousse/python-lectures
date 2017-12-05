#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# We first import internal and external modules
# Then we import our own modules
import argparse
from src.users import getUsersToCallToday
from src.today import getToday

# Then we declare constants.
API_USERS = "https://jsonplaceholder.typicode.com/users"


# Then we create the main function (the name is a convention).
def main(param1, param2):
    # We define docstrings in each function !!!
    """
    Main function of simple_project. Display the current date and the users to call.

    """
    print("Current params:", param1, param2)
    print("Current date:", getToday())
    print("Users to call today:", getUsersToCallToday(API_USERS))


# This condition is True only if the script is called directly.
# It's false if we import the code in another script.
if __name__ == "__main__":
    # args should be checked here.
    parser = argparse.ArgumentParser(description='A simple project')
    parser.add_argument('positional_param', type=int, help='A required parameter.')
    parser.add_argument('--optional_param', type=int, default=15, help='An optional paremeter.')
    args = parser.parse_args()
    main(args.positional_param, args.optional_param)

# We can remove this condition if we have a file __main__.py
