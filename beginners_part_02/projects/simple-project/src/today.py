#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime


def getToday():
    """
    Get the current date in str format.

    :return: The current date.
    :rtype: str
    :Example: getToday()

    """
    return datetime.now().strftime("%Y-%m-%d")
