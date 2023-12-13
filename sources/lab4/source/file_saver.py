from .interfaces.file_saver import FileSaver

class MyFileSaver(FileSaver):
    """Concrete implementation of the FileSaver abstract class.

    This class provides methods for saving ASCII art to a file.
    """

    def save_to_file(self, art_text, filename):
        """Save ASCII art to a file.

        Args:
            art_text (str): The ASCII art to be saved.
            filename (str): The name of the file to which the ASCII art will be saved.
        """
        with open(filename, "w", encoding="utf-8") as file:
            file.write(art_text)
        print(f"ASCII art has been saved to {filename}")
        