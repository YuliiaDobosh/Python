from abc import ABC, abstractmethod
from .program import Program 

class ASCIIArtGenerator(Program, ABC):
    @abstractmethod
    def generate(self):
        pass