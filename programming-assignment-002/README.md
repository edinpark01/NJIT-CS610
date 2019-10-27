# Programming Assignment 2

On this assignment we will get exposed to recursive descent traversall and creation of
a Expression Tree.

## Exercise Instructions

Consider the following expression BNF:

``` text
<expression> ::= <term> + <expression> | <term> - <expression> | <term>
<term>       ::= <factor> * <term> | <factor> / <term> | <factor>
<factor>     ::= <digit> | (  <expression>  )
<digit>      ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

```

1. Using recursive descent, and only recursive descent, scan expressions that adhere to the BNF above to build their expression tree.

2. Write an integer valued function that scans the tree to evaluate the expression represented by the tree.

**FUNNY NOTE from Professor/TA**:

There are plenty of clever programs online that you can download to evaluate arithmetic expression tree; if you want zero in this assignment, download one and submit it as programming assignment #2; if you want a grade greater than zero, please follow our instructions. Thanks.

### Input

A numeric expression adhering to this BNF.

``` python
input1 = "7 - 5 + 2"
input2 = "6 / ( 8 + 1 ) / 3"
input3 = "( (5 - 1 ) * 3) / ( 8 / 4 / 2 ) - ( 9 - 5 - 2 + 6 )"
```

### Output

Some representation of the expression tree.
The result of evaluating the expression.

``` python
out1 = 0
out2 = 2.0
out3 = -9.0
```
