from .interfaces import ascii_art_generator
from .interfaces import file_saver
from .interfaces import input_handler
from .interfaces import output_handler
import pyfiglet
import termcolor
class ASCIIArtGenerator (ascii_art_generator.ASCIIArtGenerator):

    def __init__(self, input_handler:input_handler.InputHandler, 
             output_handler:output_handler.OutputHandler, 
             file_saver:file_saver.FileSaver):
        self.input_handler = input_handler
        self.output_handler = output_handler
        self.file_saver = file_saver

    def generate(self):
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


    def run(self):
        while True:
            self.generate()
            
            continue_choice = self.input_handler.yes_or_no("Do you want to continue? (yes/no): ")
            if not continue_choice:
                break
