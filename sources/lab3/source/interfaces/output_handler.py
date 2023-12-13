"""
Module: my_output_module
This module defines an abstract base class for handling the display of ASCII art.
"""
from abc import ABC, abstractmethod

class OutputHandler(ABC):
    """Abstract base class for handling the display of ASCII art."""

    @abstractmethod
    def display(self, art_text):
        """Display the ASCII art.

        This method is responsible for displaying the generated ASCII art.

        Args:
            art_text (str): The ASCII art to be displayed.
        """
