import sys

def error_message_detail(error):
    """
    Generate a detailed error message.

    Args:
        error: The error object.

    Returns:
        str: A formatted error message including line number and filename.
    """
    _, _, exc_info = sys.exc_info()
    filename = exc_info.tb_frame.f_code.co_filename
    lineno = exc_info.tb_lineno
    error_message = "Error encountered in line no [{}], filename : [{}], saying [{}]".format(lineno, filename, error)
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        """
        Initialize a CustomException with a detailed error message.

        Args:
            error_message (str): The error message to be logged.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self) -> str:
        """Return the detailed error message."""
        return self.error_message