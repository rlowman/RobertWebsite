from .exceptions import UnsolvableEquationError

validOperators = ['+', '-', '/', '!',
                  '*', '%', '^']

allValidSymbols = ['0', '1', '2', '3',
                   '4', '5', '6', '7',
                   '8', '9', 'A', 'B',
                   'C', 'D', 'E', 'F',
                   '+', '-', '/', '!',
                   '*', '%', '^', 'b',
                   'x', 'o']

def equationSplit(eqn):
    eq = eqn.split()
    invalidSymbols = []
    index = 0
    valid = True
    # Checks all symbols in given equation to ensure no invalid symbols were
    # passed
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
    return eq

def solveInFix(infixEqn):
    """Solves the given equation in infixNotation, or polish notation.
    Will throw an Unsolvable Equations Error for equations that are not
    in proper polish notiation
    """
    eq = infixEqn
    valid = True
    try:
        eq = equationSplit(eq)
    except UnsolvableEquationError:
        valid = False
        raise
    index = 0
    operandStack = []
    operatorStack = []
    if valid:
        pendingOperand = True
        for token in eq:
            if token in validOperators:
                pendingOperand = False
                operatorStack.append(token)
            else:
                operand = token
                if pendingOperand:
                    while len(operandStack) > 0:
                        if len(operatorStack) > 0:
                            operator = operatorStack.pop()
                            if operator == '!':
                                x = 1
                            else:
                                arg1 = operandStack.pop()
                                if operator == '+':            # Addition
                                    operand = arg1 + operand
                                elif operator == '-':          # Subtraction
                                    operand = arg1 - operand
                                elif operator == '/':          # Division
                                    operand = arg1 / operand
                                elif operator == '*':          # Multiplication
                                    operand = arg1 * operand
                                elif operator == '^':          # Power
                                    operand = arg1 ^ operand
                                else:                       # Modulus
                                    operand = arg1 % operand
                        else:
                            raise UnsolvableEquationError("This equation contains too many operators.")
                operandStack.append(operand)
                pendingOperand = True
        result = operandStack.pop()
        return result

def solvePostFix(postfixEqn):
    """Solves the given equation in infixNotation, or polish notation.
    Will throw an Unsolvable Equations Error for equations that are not
    in proper polish notiation
    """
    eq = postfixEqn
    valid = True
    try:
        eq = equationSplit(eq)
    except UnsolvableEquationError:
        valid = False
        raise
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
