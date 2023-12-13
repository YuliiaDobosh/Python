from .interfaces.input_handler import InputHandler

class InputHandler(InputHandler):
    """Concrete implementation of the InputHandler abstract class.

    This class provides methods for interacting with the user to gather input
    for ASCII art generation.
    """
    def get_text(self):
        """Get user input for the word or phrase."""
        return input("Enter the word or phrase for ASCII art: ")

    # Select a color from a predefined list
    def select_color(self):
        """Select a color from a predefined list."""
        colors = ["red", "green", "yellow", "blue", "grey", "cyan", "white"]
        for i, color in enumerate(colors):
            print(f"{i + 1}. {color}")
        choice = self.get_number("Select a color by number: ")
        return colors[choice - 1]

    # Ask a yes/no question and return True for 'yes', False for 'no'
    def yes_or_no(self, question):
        """Ask a yes/no question and return True for 'yes', False for 'no'."""
        answer = input(f"{question} (yes/no): ").strip().lower()
        return answer == 'yes'

    # Display a list of options and return the user's choice
    def choose(self, options):
        """Display a list of options and return the user's choice."""
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        choice = self.get_number("Make a choice by number: ")
        return options[choice - 1]

    # Prompt the user for input with a custom prompt
    def write_answer(self, prompt):
        """Prompt the user for input with a custom prompt."""
        return input(prompt)

    # Get a number from the user, handling invalid input with a loop
    def get_number(self, prompt):
        """Get a number from the user, handling invalid input with a loop."""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")
                