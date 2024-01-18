# parser.py
# parser for Cal
# Andrew Poock

from pprint import pprint
import sys
from checker import (PROG,
                     isnum,
                     isstring,
                     isid,
                     check_syntax,
                     tokenize,  # note: this was added, see solution.
                     )

"""Representation:

Each node of the AST consists of an "operation" and a list
of children that the operation is applied to. This structure is
represented as a Python list where the first item in the list is the
operation (a string) and the remaining items in the list are the
children. Basic operand nodes (string, number, id) have a type descriptor
with the token as a single child (e.g 32.4 is represented as: ["number"
"32.4"].

Here's the complete AST for our quadratic solver:

['program',
 ['print', ['string', 'Welcome to the quadratic equation solver']],
 ['print'],
 ['input', 'Enter the coefficients (a, b, c):', 'a', 'b', 'c'],
 [':=',
  'discrt',
  ['call',
   'sqrt',
   ['-',
    ['^', ['id', 'b'], ['number', '2']],
    ['*', ['*', ['number', '4'], ['id', 'a']], ['id', 'c']]]]],
 [':=',
  'root1',
  ['/',
   ['-', ['-', ['id', 'b']], ['id', 'discrt']],
   ['*', ['number', '2'], ['id', 'a']]]],
 [':=',
  'root2',
  ['/',
   ['+', ['-', ['id', 'b']], ['id', 'discrt']],
   ['*', ['number', '2'], ['id', 'a']]]],
 ['print',
  ['string', 'The roots are'],
  ['id', 'root1'],
  ['string', 'and'],
  ['id', 'root2']],
 ['print'],
 ['print', ['string', 'Thanks for using the quadratic solver!']]]
"""


# Functions to construct the AST. The program is syntax-checked before
# being tokenized, so the parsing functions do not need to worry about
# doing syntax checking.

def parse_program(tokens):
    """ <S> ::= {<STMT>;} """
    ast = ["program"]
    while not tokens.done:
        ast.append(parse_statement(tokens))
        tokens.get()  # ";"
    return ast


def parse_statement(tokens):
    """ <STMT> ::= <INPUT_STMT> | <PRINT_STMT> | <ASSIGN_STMT>  """
    if tokens.peek() == "input":
        return parse_input_statement(tokens)
    elif tokens.peek() == "print":
        return parse_print_statement(tokens)
    else:
        return parse_assignment_statement(tokens)
    

def parse_input_statement(tokens):
    """ <INPUT_STMT> ::= input <string> [<id> {, <id>}] """
    tree = [tokens.get()]
    tree.append(tokens.get().replace('"', ''))
    if isid(tokens.peek()):
        tree.append(tokens.get())
        while tokens.peek() == ",":
            tokens.get()
            tree.append(tokens.get())
    return tree


def parse_print_statement(tokens):
    """ <PRINT_STMT> ::= print [<PRINTABLE> {, <PRINTABLE>)}]"""
    tree = [tokens.get()]
    if tokens.peek() == ";":
        return tree
    tree.append(parse_printable(tokens))
    while tokens.peek() == ",":
        tokens.get()
        tree.append(parse_printable(tokens))
    return tree


def parse_printable(tokens):
    """ <PRINTABLE> ::= <str> | <E> """
    if isstring(tokens.peek()):
        return ["string", tokens.get().replace('"', '')]
    return parse_expression(tokens)


def parse_assignment_statement(tokens):
    """ <ASSIGN_STMT> ::= <id> := <E> """
    tree = [":=", tokens.get()]
    tokens.get()
    tree.append(parse_expression(tokens))
    return tree


def parse_expression(tokens):
    """ <E> ::= <E1> {(+|-) <E1>} """
    expr = parse_e1(tokens)
    while tokens.peek() in ["+","-"]:
        expr = [tokens.get(), expr, parse_e1(tokens)]
    return expr


def parse_e1(tokens):
    """  <E1> ::= <E2> {(*|/) <E2>} """
    e1 = parse_e2(tokens)
    while tokens.peek() in ["*","/"]:
        e1 = [tokens.get(), e1, parse_e2(tokens)]
    return e1


def parse_e2(tokens):
    """ <E2> ::= {-} <E3> """
    count = 0
    while tokens.peek() == "-":
        count += 1
        tokens.get()
    if count % 2 != 0:
        return ["-", parse_e3(tokens)]
    return parse_e3(tokens)


def parse_e3(tokens):
    """ <E3> ::= <E4> | <E4> ^ <E3> """
    e3 = parse_e4(tokens)
    if tokens.peek() == "^":
        e3 = [tokens.get(), e3, parse_e3(tokens)]
    return e3


def parse_e4(tokens):
    """ <E4> ::= <number> | (<E>) | <id> [( [<E> {, <E>}] )] """
    if isnum(tokens.peek()):
        return ["number", tokens.get()]
    elif tokens.peek() == "(":
        tokens.get()
        exp = parse_expression(tokens)
        tokens.get()
        return exp
    else:
        e4 = []
        id = tokens.get()
        if tokens.peek() == "(":
            e4.append("call")
            e4.append(id)
            tokens.get()
            if tokens.peek() != ")":
                e4.append(parse_expression(tokens))
                while tokens.peek() == ",":
                    tokens.get()
                    e4.append(parse_expression(tokens))
            tokens.get()
            return e4
        e4.append("id")
        e4.append(id)
        return e4


def test_parser():
    ast = parse_program(tokenize(PROG))
    pprint(ast)


if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        progstr = infile.read()
    check_syntax(progstr)
    ast = parse_program(tokenize(progstr))
    pprint(ast)
