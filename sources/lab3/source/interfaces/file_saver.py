"""
File Saver Module

This module defines the abstract base class FileSaver, which inherits from ABC.
It declares an abstract method 'save_to_file' that must be implemented by concrete subclasses.
"""
from abc import ABC, abstractmethod

class FileSaver(ABC):
    """
    Abstract base class for saving ASCII art to a file.

    This class defines an abstract method 'save_to_file' that must be implemented
    by concrete subclasses for saving ASCII art to a file.
    """

    @abstractmethod
    def save_to_file(self, art_text, filename):
        """
        Abstract method to save ASCII art to a file.

        Concrete subclasses must implement this method to provide specific
        functionality for saving ASCII art to a file.

        :param art_text: The ASCII art to be saved.
        :type art_text: str
        :param filename: The name of the file to save the ASCII art to.
        :type filename: str
        """
