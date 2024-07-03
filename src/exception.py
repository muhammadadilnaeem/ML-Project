import sys  # sys is a built-in module in python which provides access to some variables used or maintained by the interpreter at runtime.
import logging
from logger import LOG_FILE_PATH  # Import the log file path from logger.py

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message including the file name, line number, and error message.
    
    Args:
        error (Exception): The error/exception object.
        error_detail (sys): The sys module instance to fetch the current exception traceback.
    
    Returns:
        str: A detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # exc_info() returns the exception type, value, and traceback object associated with the current exception
    
    file_name = exc_tb.tb_frame.f_code.co_filename  # f_code.co_filename gives the name of the file where the exception occurred and tb_frame gives the traceback object
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message

class CustomException(Exception):
    """
    Custom exception class that includes detailed error messages.
    
    Args:
        error_message (str): The original error message.
        error_detail (sys): The sys module instance to fetch the current exception traceback.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        logging.error(self.error_message)  # Log the error message
    
    def __str__(self):
        """
        Returns the detailed error message.
        
        Returns:
            str: The detailed error message.
        """
        return self.error_message

# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e, sys)
