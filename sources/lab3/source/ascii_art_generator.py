import logging
import pyfiglet
import termcolor

from .interfaces import ascii_art_generator
from .interfaces import file_saver
from .interfaces import input_handler
from .interfaces import output_handler

class ASCIIArtGenerator(ascii_art_generator.ASCIIArtGenerator):
    """Class for generating ASCII art."""

    def __init__(self, input_handler_instance: input_handler.InputHandler, 
                 output_handler_instance: output_handler.OutputHandler, 
                 file_saver_instance: file_saver.FileSaver):
        """Initialize the ASCIIArtGenerator."""
        self.input_handler = input_handler_instance
        self.output_handler = output_handler_instance
        self.file_saver = file_saver_instance
        logging.info("ASCIIArtGenerator ініціалізовано")

    def generate(self):
        """Generate ASCII art based on user input.

        This method prompts the user for text, font, and color preferences,
        generates ASCII art using pyfiglet and termcolor, and optionally
        displays a preview or saves the generated art to a file.
        """
        logging.info("Початок генерації ASCII арту")

        text = self.input_handler.get_text()
        font = self.input_handler.select_font()
        color = self.input_handler.select_color()
        
        ascii_art = pyfiglet.Figlet(font=font)
        art_text = ascii_art.renderText(text)
        art_text = termcolor.colored(art_text, color)
        if self.input_handler.yes_or_no ("Do you like to see a preview? "):
            self.output_handler.display(art_text)
        if self.input_handler.yes_or_no ("Do you like to save an art? "):       
            self.file_saver.save_to_file(art_text, f"{self.input_handler.write_answer('Enter file name: ')}.txt")

        logging.info("ASCII арт створено")

    def run(self):
        """Run the ASCII art generation process in a loop.

        This method repeatedly calls the generate method and prompts the user
        if they want to continue generating ASCII art.
        """
        while True:
            self.generate()
            
            continue_choice = self.input_handler.yes_or_no("Do you want to continue? (yes/no): ")
            if not continue_choice:
                logging.info("Користувач завершив роботу з ASCIIArtGenerator")
                break