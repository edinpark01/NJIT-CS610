""" 
    Author:     Braulio Tonaco
    Date:       10/25/2019
    Class:      CS610
    College:    NJIT
    Assignment: Programming Assignment 002
    
    I consider builders.py the "meat" of the programming 
    assignment 2, it contains the functions that will be used
    for a recursive descent approach to create and later evaluate
    an expression tree.

    It will create a Expression Tree for the BNF grammar below:

    <expression> ::= <term> + <expression> | <term> - <expression> | <term>
    <term>       ::= <factor> * <term> | <factor> / <term> | <factor>
    <factor>     ::= <digit> | ( <expression> )
    <digit>      ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""
from classes import ExpressionTree, TermTree, FactorTree, Digit

from application_constants import TOKEN, OPS

def expression(): 
    """ 
    <expression> ::= <term> + <expression> | <term> - <expression> | <term> 
    """
    global TOKEN

    root_expression_tree = ExpressionTree()
    term_tree = term()

    if TOKEN == '+' or TOKEN == '-': 
        root_expression_tree.data  = TOKEN.getCurrentToken()
        
        TOKEN.getNextToken()
        root_expression_tree.left  = term_tree 
        root_expression_tree.right = expression()  
    else:
        root_expression_tree = term_tree
    
    return root_expression_tree


def term():
    """
    <term> ::= <factor> * <term> | <factor> / <term> | <factor>
    """
    global TOKEN

    root_term_tree = TermTree()
    factor_tree = factor()

    if TOKEN == '*' or TOKEN == '/':
        root_term_tree.data  = TOKEN.getCurrentToken()
        
        TOKEN.getNextToken()
        root_term_tree.left  = factor_tree
        root_term_tree.right = term()
    else:
        root_term_tree = factor_tree

    return root_term_tree


def factor():
    """
    <factor> ::= <literal> | ( <expression> )
    """
    global TOKEN

    root_factor_tree = FactorTree()

    if TOKEN == '(':
        TOKEN.getNextToken()
        root_factor_tree = expression()

        if TOKEN != ')':
            raise Exception("Missing closing parenteshis ')'")

        TOKEN.getNextToken()

    elif TOKEN.getCurrentToken() in "0123456789":
        root_factor_tree.data = TOKEN.getCurrentToken()
        TOKEN.getNextToken()

    return root_factor_tree

