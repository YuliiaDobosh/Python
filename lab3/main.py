from .source.ascii_art_generator import ASCIIArtGenerator
from .source.input_handler import InputHandler
from .source.output_handler import OutputHandler
from .source.file_saver import FileSaver

def main():


    input_handler = InputHandler()  
    output_handler = OutputHandler()  
    
    file_saver = FileSaver()  

    art_generator = ASCIIArtGenerator(input_handler, output_handler, file_saver)
    art_generator.run()

if __name__ == "__main__":
    main()