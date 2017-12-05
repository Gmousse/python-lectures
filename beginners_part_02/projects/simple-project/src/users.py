#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import requests  # This is an external module


def getUsersToCallToday(api):
    """
    Return a list of users informations to call them.

    :param api: The api path used to get users.
    :type api: str
    :return: The list of users to call.
    :rtype: list
    :Example: getUsersToCallToday("https://jsonplaceholder.typicode.com/users"s)

    """
    return requests.get(api).json()
