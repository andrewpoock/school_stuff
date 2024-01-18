# parser.py
# parser for Cal
# by John Zelle, 10/2023

from pprint import pprint
import sys
from checker import (PROG,
                     isnum,
                     isstring,
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
        ast = parse_input_statement(tokens)
    elif tokens.peek() == "print":
        ast = parse_print_statement(tokens)
    else:
        ast = parse_assignment_statement(tokens)
    return ast


def parse_input_statement(tokens):
    """ <INPUT_STMT> ::= input <string> [<id> {, <id>}] """

    ast = [tokens.get()]
    ast.append(tokens.get()[1:-1])
    if tokens.peek() == ";":
        return ast
    ast.append(tokens.get())  # first <id>
    while tokens.peek() == ",":
        tokens.get()
        ast.append(tokens.get())  # another <id>
    return ast


def parse_print_statement(tokens):
    """ <PRINT_STMT> ::= print [<PRINTABLE> {, <PRINTABLE>)}]"""

    ast = [tokens.get()]  # print
    # check for bare print by looking for (but not consuming) termintating ;
    if tokens.peek() == ";":
        return ast
    ast.append(parse_printable(tokens))
    while tokens.peek() == ",":
        tokens.get()
        ast.append(parse_printable(tokens))
    return ast


def parse_printable(tokens):
    """ <PRINTABLE> ::= <str> | <E> """

    if isstring(tokens.peek()):
        return ["string", tokens.get()[1:-1]]
    else:
        return parse_expression(tokens)


def parse_assignment_statement(tokens):
    """ <ASSIGN_STMT> ::= <id> := <E> """
    ast = [":=", tokens.get()]  # <id>
    tokens.get()  # :=
    ast.append(parse_expression(tokens))
    return ast


def parse_expression(tokens):
    """ <E> ::= <E1> {(+|-) <E1>} """

    ast = parse_e1(tokens)
    while tokens.peek() in "+-":
        ast = [tokens.get(), ast, parse_e1(tokens)]
    return ast


def parse_e1(tokens):
    """  <E1> ::= <E2> {(*|/) <E2>} """

    ast = parse_e2(tokens)
    while tokens.peek() in "*/":
        ast = [tokens.get(), ast, parse_e2(tokens)]
    return ast


def parse_e2(tokens):
    """ <E2> ::= {-} <E3> """
    count = 0
    while tokens.peek() == "-":
        count = count + 1
        tokens.get()
    if count % 2 == 0:
        return parse_e3(tokens)
    return ["-", parse_e3(tokens)]


def parse_e3(tokens):
    """ <E3> ::= <E4> | <E4> ^ <E3> """

    ast = parse_e4(tokens)
    while tokens.peek() == "^":
        ast = [tokens.get(), ast, parse_e3(tokens)]
    return ast


def parse_e4(tokens):
    """ <E4> ::= <number> | (<E>) | <id> [( [<E> {, <E>}] )] """

    peek = tokens.peek()
    if isnum(peek):
        return ["number", tokens.get()]

    if peek == "(":
        tokens.get()
        expr = parse_expression(tokens)
        tokens.get()  # ")"
        return expr

    # must be bare id or function call
    id = tokens.get()
    if tokens.peek() != "(":  # must be bare id
        return ["id", id]

    # must be a function call
    tokens.get()  # consume "("
    ast = ["call", id]
    if tokens.peek() != ")":  # parse parameters
        ast.append(parse_expression(tokens))
        while tokens.peek() == ",":
            tokens.get()
            ast.append(parse_expression(tokens))
        tokens.get()  # the trailing ')'
    return ast


def test_parser():
    ast = parse_program(tokenize(PROG))
    pprint(ast)


if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        progstr = infile.read()
    check_syntax(progstr)
    ast = parse_program(tokenize(progstr))
    pprint(ast)
