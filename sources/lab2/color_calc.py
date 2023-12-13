"""
Module Description

This module contains the ColorCalculator class, which is a subclass of the Calculator class.
It adds the ability to display results with colored formatting using the termcolor library.
"""
from termcolor import colored
from .calc import Calculator

class ColorCalculator(Calculator):
    """
    A calculator class that displays results with colored formatting.

    This class inherits from the Calculator class and adds the ability
    to display results in red using the termcolor library.
    """
    def display_result(self):
        """
        Display the result with colored formatting.

        This method prints the result in red using the termcolor library.
        """
        print(colored(f"Result: {self._result}", "red"))
