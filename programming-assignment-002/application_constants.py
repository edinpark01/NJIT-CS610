"""
    Author:     Braulio Tonaco
    Date:       10/25/2019
    Class:      CS610
    College:    NJIT
    Assignment: Programming Assignment 002

    application_constants.py includes the constant values for:
    Token: 
        variable which will be used as a shared value while 
        creating the expression tree.
    
    OPS:   
        dictionary which will include lambda expressions which 
        will assist in the evaluation of the expression tree and
        make the cleaner. 
    
    TEST_CASES:
        list variable which will contain all test cases assigned 
        by our TA. 
"""

from classes import Token

TOKEN = Token()

OPS = {
    "+": lambda x,y: x + y, 
    "-": lambda x,y: x - y,
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y
}

TEST_CASES = [
    "(7 + 5) - 2",
    "7 - 5 + 2",
    "6 / ( 8 + 1 ) / 3",
    "( (5 - 1 ) * 3) / ( 8 / 4 / 2 ) - ( 9 - 5 - 2 + 6 )",
]

