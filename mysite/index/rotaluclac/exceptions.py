class Error(Exception):
    """Base class for other exceptions"""
    pass

class UnsolvableEquationError(Error):
    """Raised when an invalid equation is given"""
    def __init__(self, message):
        super(UnsolvableEquationError, self).__init__(message)
