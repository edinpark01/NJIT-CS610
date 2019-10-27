"""
    Author:     Braulio Tonaco
    Date:       10/25/2019
    Class:      CS610
    College:    NJIT
    Assignment: Programming Assignment 002
"""

class Token():

    def __init__(self):
        self.token = None
        self.__expression = None
        self.__pointer = 0
        
    def getCurrentToken(self):
        """ Returns the current token value """
        return self.token

    def getNextToken(self):
        """ Sets subsequent token value from expression """
        if self.__pointer + 1 >= self.__expression.__len__():
            self.token = None
        else:      
            self.__pointer += 1
            self.token = self.__expression[self.__pointer]
    
    def setToken(self, expression):
        """ Sets expression token to create Expression Tree """
        self.__expression = expression
        self.token = self.__expression[self.__pointer]

    def cleanUp(self):
        """ Cleans token object value for next test case"""
        self.token = None
        self.__expression = None
        self.__pointer = 0
        
    def __repr__(self):
        """ Object representation """ 
        return self.token

    def __eq__(self, some_token):
        """ Overloaded operation for '==' boolean comparisons """
        return self.token == some_token


class BaseTree:
    def __init__(self):
        self.left  = None
        self.data  = None
        self.right = None
    
    def isLeaf(self):
        return self.left  is None and \
               self.right is None
    
    def isRoot(self):
        return  self.left  is not None or \
                self.right is not None


class ExpressionTree(BaseTree):
    def __init__(self):
        BaseTree.__init__(self)

class TermTree(BaseTree):
    def __init__(self):
        BaseTree.__init__(self)

class FactorTree(BaseTree):
    def __init__(self):
        BaseTree.__init__(self)

class Digit(BaseTree):
    def __init__(self):
        self.data

