import Stack
import exceptions

class Calculator():

    validBaseSymbols = ['b', 'x', 'o']

    validOperators = ['+', '-', '/',
                      '*', '%', '^',
                      '!']
    validOctal = ['0', '1', '2', '3',
                  '4', '5', '6', '7',
                  '8']
    validDecimal = ['0', '1', '2', '3',
                    '4', '5', '6', '7',
                    '8', '9']
    validHexadecimal = ['0', '1', '2', '3',
                        '4', '5', '6', '7',
                        '8', '9', 'A', 'B',
                        'C', 'D', 'E', 'F']

    allValidSymbols = set(validBaseSymbols | validOperators | validHexadecimal)

    def solve(self, postfixEqn, printBase):
        eq = postfixEqn.split()
        valid = True
        index = 0
        for temp in eq:
            for char in temp:
                if char not in allValidSymbols:
                    raise InvalidSymbolError(char)
                    valid = False
            if valid:
                try:
                    if temp not in validOperators:
                        eq[index] = valiateToken
                except InvalidNumberFormat:
                    valid = False
                    raise
            index += 1
        done = False
        index = 0
        stack = []
        if valid:
            for token in eq:
                if(token in validOperators):
                    # If the equation is a factorial, only one argument is needed
                    if token == '!':
                        # TODO factorial function
                    else:
                        if not stack:
                            raise InvalidEquationError("Too many operators")
                        else:
                            first = stack.pop()
                            second = stack.pop()
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
                raise InvalidEquationError("Too many operators")
            elif len stack > 1:
                raise InvalidEquationError("Too many operands")
            else:
                printString = stack.pop()

    
    def validateToken(self, theToken):
        valid = False
        base = 0
        negative = False
        if startswith(theToken, '-'):
            negative = True
            theToken = theToken[1:]
        if startswith(theToken, '0b'):
            base = 2
        elif startswith(theToken, '0o'):
            base = 8
        elif startswith(theToken, '0x'):
            base = 16
        else:
            base = 10
        try:
            result = int(theToken, base)
            if negative:
                result = result * -1
            return result
        except ValueError:
            raise InvalidNumberFormat(theToken)
