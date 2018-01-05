from exceptions import UnsolvableEquationError

validOperators = ['+', '-', '/', '!',
                  '*', '%', '^']

allValidSymbols = ['0', '1', '2', '3',
                   '4', '5', '6', '7',
                   '8', '9', 'A', 'B',
                   'C', 'D', 'E', 'F',
                   '+', '-', '/', '!',
                   '*', '%', '^', 'b',
                   'x', 'o']

def solveInFix(infixEqn):
    pass

def solvePostFix(postfixEqn):
    eq = postfixEqn.split()
    invalidSymbols = []
    index = 0
    valid = True
    for temp in eq:
        for char in temp:
            if char not in allValidSymbols:
                invalidSymbols.append(char)
                valid = False
        if valid:
            try:
                if temp not in validOperators:
                    eq[index] = validateToken(temp)
            except UnsolvableEquationError:
                valid = False
                raise
        index += 1
    if len(invalidSymbols) > 0:
        message = "The following symbols cannot be read: "
        for c in invalidSymbols:
            message = message + c
        raise UnsolvableEquationError(message)
    index = 0
    stack = []
    if valid:
        for token in eq:
            if(token in validOperators):
                # If the equation is a factorial, only one argument is needed
                if token == '!':
                    # TODO factorial function
                    first = stack.pop()
                else:
                    if len(stack) == 0:
                        raise UnsolvableEquationError("This equation contains too many operators")
                    else:
                        arg1 = stack.pop()
                        arg2 = stack.pop()
                        result = 0
                        if token == '+':
                            result = arg2 + arg1
                        elif token == '-':
                            result = arg2 - arg1
                        elif token == '/':
                            result = arg2 / arg1
                        elif token == '*':
                            result = arg2 * arg1
                        elif token == '^':
                            result = arg2 ^ arg1
                        else:
                            result = arg2 % arg1
                        stack.append(result)
            else:
                stack.append(token)
        if len(stack) == 0:
            raise UnsolvableEquationError("This equation contains too many operators")
        elif len(stack) > 1:
            raise UnsolvableEquationError("This equation contains too many operands")
        else:
            printString = stack.pop()
            return printString

def validateToken(theToken):
    valid = False
    base = 0
    negative = False
    if theToken.startswith('-'):
        negative = True
        theToken = theToken[1:]
    if theToken.startswith('0b'):
        base = 2
    elif theToken.startswith('0o'):
        base = 8
    elif theToken.startswith('0x'):
        base = 16
    else:
        base = 10
    try:
        result = int(theToken, base)
        if negative:
            result = result * -1
        return result
    except ValueError:
        message = theToken + " was declared in base " + str(base) + ",\n however a symbol was not recognized in this base"
        raise UnsolvableEquationError(message)
