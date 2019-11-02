""" 
    Author:     Braulio Tonaco
    Date:       10/25/2019
    Class:      CS610
    College:    NJIT
    Assignment: Programming Assignment 002
"""

import logging

from builders import expression
from application_constants import TOKEN, TEST_CASES
from utils import evaluate_tree, print_results

if __name__ == "__main__":

    for test in TEST_CASES:
        expr = test.replace(' ', '')    # We use str.replace() function to 
                                        # remove all whitespace characters 
                                        # from expression if they exist.

        # STEP 1: Set token 
        TOKEN.setToken(expr)
        
        # STEP 2: Initialize/Create Expression Tree
        tree = expression()

        # STEP 4: Evaluate Tree
        result = evaluate_tree(tree)

        # STEP 5: Print Results
        print_results(tree, result, expr)

        # STEP 6: Clean up token for next iteration
        TOKEN.cleanUp()

