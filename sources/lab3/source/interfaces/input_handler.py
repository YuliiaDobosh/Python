"""
Input Handler Module

This module defines the abstract base class InputHandler, which inherits from ABC.
It declares several abstract methods for handling user input in an ASCII Art generator.
"""
from abc import ABC, abstractmethod

class InputHandler(ABC):
    """
    Abstract base class for handling user input in an ASCII Art generator.

    Concrete subclasses must implement the abstract methods to provide specific
    functionality for obtaining user input.

    Example Usage:
    input_handler = MyInputHandler()
    text = input_handler.get_text()
    font = input_handler.select_font()
    color = input_handler.select_color()
    """

    @abstractmethod
    def get_text(self):
        """
        Abstract method to get text input from the user.

        Concrete subclasses must implement this method to provide specific
        functionality for obtaining text input.
        """

    @abstractmethod
    def select_font(self):
        """
        Abstract method to let the user select a font.

        Concrete subclasses must implement this method to provide specific
        functionality for font selection.
        """

    @abstractmethod
    def select_color(self):
        """
        Abstract method to let the user select a color.

        Concrete subclasses must implement this method to provide specific
        functionality for color selection.
        """

    @abstractmethod
    def yes_or_no(self, question):
        """
        Ask a yes/no question and return a boolean.

        :param question: The yes/no question to ask.
        :type question: str
        :return: True if the user answers 'yes', False otherwise.
        :rtype: bool
        """

    @abstractmethod
    def choose(self, options):
        """
        Let the user choose from a list of options.

        :param options: List of options to choose from.
        :type options: list
        :return: The user's selected option.
        """

    @abstractmethod
    def write_answer(self, prompt):
        """
        Get a string input from the user.

        :param prompt: The prompt to display to the user.
        :type prompt: str
        :return: The user's input as a string.
        :rtype: str
        """

    @abstractmethod
    def get_number(self, prompt):
        """
        Get a numeric input from the user.

        :param prompt: The prompt to display to the user.
        :type prompt: str
        :return: The user's input as a numeric value.
        :rtype: int or float
        """
