import traceback
import sys

class CustomException(Exception):

    def __init__(self, error_message: str, error_detail: Exception):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)

    @staticmethod
    def get_detailed_error_message(error_message: str, error_detail: Exception) -> str:
        """Generate detailed error message including the file and line where the exception occurred."""

        _, _, exc_tb = sys.exc_info()  # Extract the current exception information
        file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the exception occurred
        line_number = exc_tb.tb_lineno  # Get the line number of the exception

        return f"Error in {file_name}, line {line_number}: {error_message}"

    def __str__(self):
        return self.error_message
