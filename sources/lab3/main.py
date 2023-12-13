"""
Module Description: This module contains the main function to run the ASCII Art Generator.

Additional details about the module can go here.
"""

from .source.ascii_art_generator import ASCIIArtGenerator
from .source.input_handler import InputHandler
from .source.output_handler import OutputHandler
from .source.file_saver import FileSaver

def main():
    """
    Main function to run the ASCII Art Generator.

    This function initializes the necessary components (InputHandler, OutputHandler, FileSaver)
    and creates an ASCIIArtGenerator object to generate ASCII art.
    """
    input_handler = InputHandler()
    output_handler = OutputHandler()
    file_saver = FileSaver()
    art_generator = ASCIIArtGenerator(input_handler, output_handler, file_saver)
    art_generator.run()

if __name__ == "__main__":
    main()
    