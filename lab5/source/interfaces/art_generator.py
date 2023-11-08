from abc import ABC, abstractmethod
from ..interfaces.file_saver import FileSaver
from ..graphic.graphic import Graphic

class ArtGenerate(ABC):
    def __init__(self, graphic: Graphic, file_saver: FileSaver) -> None:
        super().__init__()
        self.graphic = graphic
        self.file_saver = file_saver

    @abstractmethod
    def generate_art(self):
        pass

    @abstractmethod
    def start(self):
        pass