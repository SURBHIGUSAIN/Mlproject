# for writing excception for codes. this will be same for all codes ussually .
import sys  # for provides various functions and variables that are used to manipulate different parts of the Python runtime environment
from src.loggers import logging

# custom method which returns error details at exception


def error_message_detail(error, error_detail: sys):
    # gives info like which line no , what error etcete
    _, _, exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error))
    # whenever my error raises , we will call this function with
    return error_message


class CustomException(Exception):  # inehriting parent exception
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        # whatever error message is coming from above fucntion , will be put over here
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail)
        # the error message received will be initialized to the class CustomException variable error_message
        # error detail will be tracked by sys

    # we will inehrit one more functionality
    def __str__(self):
        # whenever i'll try to print it , we will get error message here.
        return self.error_message
