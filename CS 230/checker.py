# checker.py
#  by: John Zelle 9/2023
#  syntax checker for cal

import string

DEBUG = False


def char_position_iter(str):
    """Iterate through a char sequence keeping track of line and column"""
    currpos = (1, 1)
    for ch in str:
        yield ch, currpos
        line, col = currpos
        if ch == "\n":
            currpos = line+1, 1
        else:
            currpos = line, col+1


class LookAhead:
    """ One item buffer for reading an item-position sequence """

    def __init__(self, seq):
        self.iter = iter(seq)
        self.pos = None
        self.done = False
        self._advance()

    def _advance(self):
        try:
            self.item, self.pos = next(self.iter)
            #if DEBUG:
            #    print(f"{self.pos}: read '{self.item}'")
        except StopIteration:
            self.done = True

    def peek(self):
        """ return current item """

        assert not self.done
        return self.item

    def get(self):
        """ return current item and advance to next """

        assert not self.done
        item = self.item
        self._advance()
        return item


#----------------------------------------------------------------------
# Quadratic program for testing

PROG = """
# quad.cal -- quadratic equation solver in cal

print "Welcome to the quadratic equation solver";
print;

input "Enter the coefficients (a, b, c):" a, b, c;

discrt := sqrt(b^2 - 4 * a * c);
root1 := (-b - discrt) / (2 * a);
root2 := (-b + discrt) / (2 * a);

print "The roots are", root1, "and", root2;
print;
print "Thanks for using the quadratic solver!";
"""

# -------------------------------------------------------------------
# Lexical structure: program is sequence of tokens
# Note: as is typical of lexical analysis, this grammar admits sequences
#       of tokens that are not legal programs. Its purpose is simply to
#       define the set of legal tokens.

"""
<tokens> ::= {{space} <token> {space}}
 <token> ::= + | - | * | / | ^ | '(' | ')' | ; | :=
             | <comment> | <id> | <num> | <string>
    <id> ::= <letter> {<letter> | <digit>}
   <num> ::= . <digit> {<digit>} | <digit> {<digit>} [. {<digit>}]
<string> ::= "{<char>}"
"""


def parse_tokens(programString):
    """<tokens> ::= {{space} <token> {space}}"""

    charseq = LookAhead(char_position_iter(programString))
    while True:
        while not charseq.done and charseq.peek() in string.whitespace:
            charseq.get()
        if charseq.done:
            break
        start = charseq.pos
        #if DEBUG:
        #    print(f"At {start}, {charseq.peek()}")

        token = parse_token(charseq)
        if DEBUG:
            print(f"token {start}: '{token}'")

        if token[0] != "#":  # skip comments
            yield token, start


def parse_token(charseq):
    """<token> ::= + | - | * | / | ^ | '(' | ')' | ; | , | :=
                  | <comment> | <id> | <num> | <string>
    """

    # single char token
    if charseq.peek() in "+-*/^)(;,":
        return charseq.get()

    if charseq.peek() == ":":
        return parse_assign(charseq)

    if charseq.peek() == "#":
        return parse_comment(charseq)

    if charseq.peek() in string.ascii_letters+"_":
        return parse_id(charseq)

    if charseq.peek() in string.digits+".":
        return parse_num(charseq)

    if charseq.peek() == '"':
        return parse_string(charseq)

    raise SyntaxError(f"Unrecognized token at {charseq.pos}: '{charseq.peek()}'")


def parse_assign(charseq):
    charseq.get()
    if charseq.peek() != "=":
        raise SyntaxError("Expected '=' at " + str(charseq.pos))
    else:
        charseq.get()
    return ":="


def parse_comment(chars):
    """ <comment> ::= '#' {<char>} '\n' """

    token = chars.get()
    while not chars.done and chars.peek() != "\n":
        token += chars.get()
    chars.get()
    if DEBUG:
        print(f"Comment: '{token}'")
    return token


def parse_id(chars):
    "<id> ::= <letter> {<letter> | <digit>}"

    token = chars.get()
    while (not chars.done
           and chars.peek() in string.ascii_letters+string.digits + "_"):
        token += chars.get()
    return token


def parse_num(chars):
    "<num> ::= . <digit> {<digit>} | <digit> {<digit>} [. {<digit>}]"

    if chars.peek() == ".":
        token = chars.get()
        if chars.done or chars.peek() not in string.digits:
            raise SyntaxError("Expected digit at " + str(chars.pos))
        token += chars.get()
        while not chars.done and chars.peek() in string.digits:
            token += chars.get()
        return token
    else:
        token = chars.get()
        while not chars.done and chars.peek() in string.digits:
            token += chars.get()
        if not chars.done and chars.peek() == ".":
            token += chars.get()
            while not chars.done and chars.peek() in string.digits:
                token += chars.get()
        return token


def parse_string(chars):
    """<string> ::= "{<char>}" """

    start = chars.pos
    token = chars.get()
    while chars.peek() != '"':
        token += chars.get()
        if chars.done:
            raise SyntaxError(f"run-away string starting at {start}")
    token += chars.get()
    return token


# ------------------------------------------------------------
# Phrase structure: Program is a sequence of (semi-colon terminated) statements

"""
<PROGRAM> ::= {<STMT>;}
<STMT> ::= <INPUT_STMT> | <ASSIGN_STMT> | <PRINT_STMT>
<INPUT_STMT> ::= input <str> [<id> {, <id>}]
<ASSIGN_STMT> ::= <id> := <E>
<PRINT_STMT> ::= print {<PRINTABLE>}
<PRINTABLE> ::= <str> | <E>
<E> ::= <E1> {(+|-) <E1>}
<E1> ::= <E2> {(*|/) <E2>}
<E2> ::= {-} <E3>
<E3> ::= <E4> {^ <E4>}
<E4> ::= <num> | '('<E>')' | <id> | <id>'(' [<E> {, <E>}] ')'
"""

# ------------------------------------------------------------
# Helper functions for parsing phrase structure


def expect(tokens, targets):
    """ make sure current token is in targets and consume it """
    if tokens.done:
        raise SyntaxError(f"{tokens.pos}: EOF when expecting {targets}")
    if tokens.peek() in targets:
        return tokens.get()
    else:
        raise SyntaxError(f"{tokens.pos}: {tokens.peek()} not in {targets}")


def testtoken(tokens, test, expected):
    """ make sure current token passes test and consume it """
    if tokens.done:
        raise SyntaxError(f"{tokens.pos}: Expected '{expected}' found EOF")
    if test(tokens.peek()):
        return tokens.get()
    else:
        raise SyntaxError(f"{tokens.pos}: Expected '{expected}' found '{tokens.peek()}'")


def isstring(token):
    """ test whether token is a string """
    return token[0] == '"'


def isid(token):
    """ test whether token is an id """
    return token[0] in string.ascii_letters


def isnum(token):
    """ test whether token is a number """
    return token[0] in string.digits+"."


def canget(tokens, token):
    """ check whether token is available and if so, consume it """
    if not tokens.done and tokens.peek() == token:
        tokens.get()
        return True
    return False


def safepeek(tokens, current_element):
    """ Like peek but report error if at end of tokens """
    if tokens.done:
        raise SyntaxError(f"{tokens.pos}: EOF during {current_element}")
    return tokens.peek()


def tokenize(progstr):
    """ Turn string into a LookAhead of tokens """
    return LookAhead(parse_tokens(progstr))


# ------------------------------------------------------------
# Syntax Checker following the grammar


def check_syntax(programString):
    tokens = tokenize(programString)
    check_program(tokens)


def check_program(tokens):
    """ <S> ::= {<STMT>;} """
    while not tokens.done:
        check_statement(tokens)
        expect(tokens, [";"])


def check_statement(tokens):
    """ <STMT> ::= <INPUT_STMT> | <PRINT_STMT> | <ASSIGN_STMT>  """

    if tokens.peek() == "input":
        check_input_statement(tokens)
    elif tokens.peek() == "print":
        check_print_statement(tokens)
    else:
        check_assignment_statement(tokens)


def check_input_statement(tokens):
    """ <INPUT_STMT> ::= input <string> [<id> {, <id>}] """

    expect(tokens, ["input"])
    testtoken(tokens, isstring, "a string")
    if safepeek(tokens, "statement") == ";":
        return
    testtoken(tokens, isid, "id")
    while canget(tokens, ","):
        testtoken(tokens, isid, "id")


def check_print_statement(tokens):
    """ <PRINT_STMT> ::= print [<PRINTABLE> {, <PRINTABLE>)}]"""

    expect(tokens, "print")
    # check for bare print by looking for (but not consuming) termintating ;
    if not tokens.done and tokens.peek() == ";":
        return
    check_printable(tokens)
    while canget(tokens, ","):
        check_printable(tokens)


def check_printable(tokens):
    """ <PRINTABLE> ::= <str> | <E> """

    if isstring(safepeek(tokens, "string or expression")):
        tokens.get()
    else:
        check_expression(tokens)


def check_assignment_statement(tokens):
    """ <ASSIGN_STMT> ::= <id> := <E> """
    testtoken(tokens, isid, "id")
    expect(tokens, [":="])
    check_expression(tokens)


def check_expression(tokens):
    """ <E> ::= <E1> {(+|-) <E1>} """

    check_e1(tokens)
    while canget(tokens, "+") or canget(tokens, "-"):
        check_e1(tokens)


def check_e1(tokens):
    """  <E1> ::= <E2> {(*|/) <E2>} """

    check_e2(tokens)
    while canget(tokens, "*") or canget(tokens, "/"):
        check_e2(tokens)


def check_e2(tokens):
    """ <E2> ::= {-} <E3> """
    while canget(tokens, "-"):
        pass
    check_e3(tokens)


def check_e3(tokens):
    """ <E3> ::= <E4> {^ <E4>} """
    check_e4(tokens)
    while canget(tokens, "^"):
        check_e4(tokens)


def check_e4(tokens):
    """ <E4> ::= <number> | (<E>) | <id>[( [<E> {, <E>}] )] """

    token = safepeek(tokens, "expression")
    if isnum(token):
        tokens.get()
    elif canget(tokens, "("):
        check_expression(tokens)
        expect(tokens, [")"])
    else: # must be bare id or function call
        testtoken(tokens, isid, "id")
        if canget(tokens, "("):  # function call
            if not canget(tokens, ")"):
                check_expression(tokens)
                while canget(tokens, ","):
                    check_expression(tokens)
                expect(tokens, ")")


def test_lexer():
    global DEBUG
    DEBUG = True
    print(list(parse_tokens(PROG)))

def test_checker():
    global DEBUG
    DEBUG = True
    check_syntax(PROG)


# ------------------------------------------------------------
# syntax checker code to run on external file
if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as infile:
        programstr = infile.read()
    if "-d" in sys.argv:
        DEBUG = True
    check_syntax(programstr)
