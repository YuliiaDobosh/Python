from abc import ABC, abstractmethod
from ..interfaces.input_handler import InputHandler
from ..interfaces.file_saver import FileSaver
from ..graphic.graphic import Graphic

class ArtGenerate(ABC):
    """Abstract base class for ASCII art generation.

    This class defines the common interface for generating ASCII art.
    """

    def __init__(self, input_handler: InputHandler, graphic: Graphic,
    file_saver: FileSaver) -> None:
        """Initialize the ArtGenerate object."""
        super().__init__()
        self.input_handler = input_handler
        self.graphic = graphic
        self.file_saver = file_saver

    @abstractmethod
    def generate_shape(self):
        """Abstract method to generate a graphical shape."""

    @abstractmethod
    def generate_art(self):
        """Abstract method to generate ASCII art."""

    @abstractmethod
    def start(self):
        """Abstract method to start the ASCII art generation process."""
        