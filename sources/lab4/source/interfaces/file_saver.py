from abc import ABC, abstractmethod

class FileSaver(ABC):
    """Abstract base class for saving ASCII art to a file.

    This class defines the common interface for saving ASCII art to a file.
    """

    @abstractmethod
    def save_to_file(self, art_text, filename):
        """Abstract method to save ASCII art to a file.

        Args:
            art_text (str): The ASCII art to be saved.
            filename (str): The name of the file to which the ASCII art will be saved.
        """
