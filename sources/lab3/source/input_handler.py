"""
ASCII Art Generator Input Handler Module

This module provides a concrete implementation of the InputHandler interface 
for obtaining user input in an ASCII art generator.
"""
import pyfiglet
from .interfaces import input_handler

class InputHandler(input_handler.InputHandler):
    """
    Concrete implementation of the InputHandler interface for obtaining 
    user input in an ASCII art generator.
    Example Usage:
    input_handler = InputHandler()
    text = input_handler.get_text()
    font = input_handler.select_font()
    color = input_handler.select_color()
    answer = input_handler.yes_or_no("Do you want to continue?")
    choice = input_handler.choose(["Option 1", "Option 2", "Option 3"])
    user_input = input_handler.write_answer("Enter something: ")
    number = input_handler.get_number("Enter a number: ")
    """

    def get_text(self):
        """
        Get text input from the user.

        :return: The user-entered text.
        :rtype: str
        """
        return input("Enter the word or phrase for ASCII art: ")

    def select_font(self):
        """
        Let the user select a font.

        :return: The selected font.
        :rtype: str
        """
        fonts = pyfiglet.FigletFont.getFonts()
        for i, font in enumerate(fonts):
            print(f"{i + 1}. {font}")
        choice = self.get_number("Select a font by number: ")
        return fonts[choice - 1]

    def select_color(self):
        """
        Let the user select a color.

        :return: The selected color.
        :rtype: str
        """
        colors = ["red", "green", "yellow", "blue", "grey", "cyan", "white"]
        for i, color in enumerate(colors):
            print(f"{i + 1}. {color}")
        choice = self.get_number("Select a color by number: ")
        return colors[choice - 1]

    def yes_or_no(self, question):
        """
        Ask a yes/no question and return a boolean.

        :param question: The yes/no question to ask.
        :type question: str
        :return: True if the user answers 'yes', False otherwise.
        :rtype: bool
        """
        answer = input(f"{question} (yes/no): ").strip().lower()
        return answer == 'yes'

    def choose(self, options):
        """
        Let the user choose from a list of options.

        :param options: List of options to choose from.
        :type options: list
        :return: The user's selected option.
        """
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        choice = self.get_number("Make a choice by number: ")
        return options[choice - 1]

    def write_answer(self, prompt):
        """
        Get a string input from the user.

        :param prompt: The prompt to display to the user.
        :type prompt: str
        :return: The user's input as a string.
        :rtype: str
        """
        return input(prompt)

    def get_number(self, prompt):
        """
        Get a numeric input from the user.

        :param prompt: The prompt to display to the user.
        :type prompt: str
        :return: The user's input as a numeric value.
        :rtype: int
        """
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")
