#!/usr/bin/python3
"""100-my_int.py
"""


class MyInt(int):
    """ Class MyInt that inherits from class int"""

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)
