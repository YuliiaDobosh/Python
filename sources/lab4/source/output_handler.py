"""
Module: my_output_module
This module defines a concrete implementation of the OutputHandler class.
"""

from .interfaces.output_handler import OutputHandler

class MyOutputHandler(OutputHandler):
    """Concrete implementation of the OutputHandler class."""
    def display(self, string: str):
        """Display the given string.

        This method prints the given string to the console without adding a newline.

        Args:
            string (str): The string to be displayed.
        """
        print(string, end='')
