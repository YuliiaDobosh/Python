from .source.art_generator import ArtGenerate
from .source.input_handler import InputHandler
from .source.graphic.graphic import Graphic
from .source.file_saver import FileSaver

def main():
    art_gen = ArtGenerate(InputHandler(), Graphic(), FileSaver())
    art_gen.start()

if "__main__" == __name__:
    main()