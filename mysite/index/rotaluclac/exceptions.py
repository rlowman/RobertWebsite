class Error(Exception):
    """Base class for other exceptions"""
    pass

class InvalidSymbolError(Error):
    """Raised when an invalid symbol is given"""
    pass

class InvalidEquationError(Error):
    """Raised when an invalid equation is given"""
    pass

class InvalidNumberFormat(Error):
    def __init__(self, message, token):
        super(InvalidNumberFormat, self).__init__(message)
        self.token = token
