"""
Output Handler Module

This module provides a concrete implementation of the OutputHandler interface 
for displaying ASCII art.
"""
from .interfaces import output_handler

class OutputHandler(output_handler.OutputHandler):
    """
    Concrete implementation of the OutputHandler interface for displaying ASCII art.
    """

    def display(self, art_text):
        """
        Display the provided ASCII art text.

        :param art_text: The ASCII art text to be displayed.
        :type art_text: str
        """
        print(art_text)
