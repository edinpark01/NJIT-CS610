"""
    Author:     Braulio Tonaco
    Date:       10/25/2019
    Class:      CS610
    College:    NJIT
    Assignment: Programming Assignment 002

    utils.py has the helper functions to fullfill 
    programming assignment 2 requirements. It has functions
    to evaluate the expression tree, do pre/post order
    traversals, and to print to console finals findings.
"""
from application_constants import OPS

def evaluate_tree(node):
    """
        evaluate_tree will simply traverse the 
        expression tree using a recursive descent
        method and return the arithmetic evaluation
        of its leaves.
    """
    if node.isLeaf():
        return int(node.data)
    
    x = evaluate_tree(node.left)
    operator = node.data
    y = evaluate_tree(node.right)

    return OPS[operator](x, y)


def print_results(some_tree, result, e):
    """
        print_results take some expression tree
        as input as well as its evaluation result
        and expression evaluated and print to 
        console the assignment required information. 
    """
    print("For expression:\t\t->\t{}".format(e))
    
    print("It evaluated to:\t->\t{}".format(result))

    print("PreOrder Traversal\t->\t", end="")
    __pre_order(some_tree)
    
    print()
    print("PostOrder Traversal\t->\t", end="")
    __post_order(some_tree)

    print("\n\n{}{}".format("*" * 50, "\n\n"))


def __pre_order(node):
    """
        __pre_order will traverse the expression
        tree and print its nodes in a PRE order 
        fashion.
    """
    
    if node and ( node.isRoot() or node.isLeaf() ):
        print(node.data, end=" ")
        __pre_order(node.left)
        __pre_order(node.right)


def __post_order(node):
    """
        __post_order will traverse the expression
        tree and print its nodes in a POST order 
        fashion.
    """
    
    if node and ( node.isRoot() or node.isLeaf() ):
        __post_order(node.left)
        __post_order(node.right)
        print(node.data, end=" ")