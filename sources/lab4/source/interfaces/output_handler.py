from abc import ABC, abstractmethod

class OutputHandler(ABC):
    """Abstract base class for displaying ASCII art.

    This class defines the common interface for displaying ASCII art.
    """

    @abstractmethod
    def display(self, string: str):
        """Abstract method to display ASCII art.

        Args:
            string (str): The ASCII art to be displayed.
        """
