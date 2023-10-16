from abc import ABC, abstractmethod

class InputHandler(ABC):
    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def select_font(self):
        pass

    @abstractmethod
    def select_color(self):
        pass

    @abstractmethod
    def yes_or_no(self, question):
        """Ask a yes/no question and return a boolean."""
        pass

    @abstractmethod
    def choose(self, options):
        """Let the user choose from a list of options."""
        pass

    @abstractmethod
    def write_answer(self, prompt):
        """Get a string input from the user."""
        pass

    @abstractmethod
    def get_number(self, prompt):
        """Get a numeric input from the user."""
        pass