"""
File Saver Module

This module provides a concrete implementation of the FileSaver interface 
for saving ASCII art to a file.
"""

from .interfaces import file_saver

class FileSaver(file_saver.FileSaver):
    """
    Concrete implementation of the FileSaver interface for saving ASCII art to a file.

    Example Usage:
    file_saver = FileSaver()
    file_saver.save_to_file(ascii_art, "output.txt")
    """

    def save_to_file(self, art_text, filename):
        """
        Save ASCII art to a file.

        :param art_text: The ASCII art to be saved.
        :type art_text: str
        :param filename: The name of the file to save the ASCII art to.
        :type filename: str
        """
        with open(filename, "w", encoding="utf-8") as file:
            file.write(art_text)
        print(f"ASCII art has been saved to {filename}")
