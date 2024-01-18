# cal.py
# interpreter for Cal
# Andrew Poock

import sys
import operator
import math

from checker import (PROG,
                     tokenize,
                     check_syntax,
                     )
from parser import parse_program

"""
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


class CalRuntimeErr(Exception):
    # Use this class to raise any run time errors
    #  e.g. raise CalRuntimeErr(f"{len(vars)} inputs required, but {len(values)} provided")
    pass


class CalInterp:
    """Interpreter for Cal"""

    def __init__(self):
        self.statement_execs = {"print": self.exec_print,
                                 "input": self.exec_input,
                                 ":=": self.exec_assign}

        self.binary_ops = {"+": operator.add,
                           "-": operator.sub,
                           "*": operator.mul,
                           "/": operator.truediv,
                           "^": operator.pow
                           }

        self.functions = {"sqrt": (1, math.sqrt)}
        self.memory = {}

    def run(self, program):
        check_syntax(program)
        stmts = parse_program(tokenize(program))[1:]
        for stmt in stmts:
            execfn = self.statement_execs[stmt[0]]
            execfn(stmt)
        print("\n**Done**")

    def eval_(self, exp):
        if exp[0] == "id":
            try:
                return self.memory[exp[1]]
            except:
                raise CalRuntimeErr(f"ERROR: {exp[1]} is not defined.")
        elif exp[0] == "number":
            return float(exp[1])
        elif exp[0] == "string":
            return str(exp[1])
        elif exp[0] == "call":
            param, func = self.functions[exp[1]]
            try:
                return func(self.eval_(exp[2]))
            except:
                raise CalRuntimeErr(f"ERROR: The {exp[1]} function could not be executed.")
        else:
            if exp[0] == "-" and len(exp) == 2:
                return self.binary_ops["*"](self.eval_(exp[1]), -1)
            return self.binary_ops[exp[0]](self.eval_(exp[1]), self.eval_(exp[2]))

    def exec_print(self, stmt):
        if len(stmt) == 1:
                print()
        else:
            out = ""
            for s in stmt[1:]:
                out += str(self.eval_(s)) + " "
            print(out)

    def exec_input(self, stmt):
        try:
            valstr = input(stmt[1] + " ")
            vallist = list(map(int, valstr.split(",")))
            for i in range(len(stmt[2:])):
                self.memory[stmt[2+i]] = vallist[i]
        except:
            raise CalRuntimeErr("ERROR: Bad input.")

    def exec_assign(self, stmt):
        self.memory[stmt[1]] = self.eval_(stmt[2])


def test():
    interp = CalInterp()
    interp.run(PROG)
    print("\nDONE")


if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        progstr = infile.read()
    CalInterp().run(progstr)
