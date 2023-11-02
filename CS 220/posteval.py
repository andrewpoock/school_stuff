# postfixeval.py
#   by: Andrew Poock

from stack import Stack


def postfixeval(tokens):
    stack = Stack()
    newitem = 0
    for item in tokens:
        if item in '+-*/':
            n1, n2 = float(stack.pop()), float(stack.pop())
            newitem = apply_op(item, n1, n2)
            stack.push(newitem)
        else:
            stack.push(item)
    return stack.top()


def apply_op(op, arg1, arg2):
    """ apply op to supplied arguments.
    pre: op in "+-*/" and both arg1 and arg2 are numbers
    """
    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    elif op == "*":
        return arg1 * arg2
    elif op == "/":
        return arg1 / arg2
    else:
        raise ValueError("Bad operator: "+op)


def main():
    print("Welcome to the postfix expression evaluator: ")
    while True:  # sentinel loop -- blank input exits
        expstr = input("Please enter your postfix expression: ")
        tokens = expstr.split()
        if tokens == []:
            break
        ans = postfixeval(tokens)
        print("The answer is", ans, "\n")


if __name__ == "__main__":
    main()
