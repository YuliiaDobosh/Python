from abc import ABC, abstractmethod
from ..interfaces.file_saver import FileSaver
from ..graphic.graphic import Graphic

class ArtGenerate(ABC):
    """Abstract base class for generating ASCII art.

    This class defines the common interface for generating and managing ASCII art.
    """

    def __init__(self, graphic: Graphic, file_saver: FileSaver) -> None:
        """Initialize the ArtGenerate object."""
        super().__init__()
        self.graphic = graphic
        self.file_saver = file_saver

    @abstractmethod
    def generate_art(self):
        """Abstract method to generate ASCII art."""

    @abstractmethod
    def start(self):
        """Abstract method to start the ASCII art generation process."""
