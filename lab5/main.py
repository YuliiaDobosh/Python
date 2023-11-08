from .source.art_generator import ArtGenerate
from .source.graphic.graphic import Graphic
from .source.file_saver import FileSaver

def main():
    art_gen = ArtGenerate(Graphic(), FileSaver())
    art_gen.start()

if __name__ == '__main__':
    main()