"""
ASCII Art Module

This module defines the abstract base class ASCIIArtGenerator, which inherits from Program and ABC.
It declares an abstract method 'generate' that must be implemented by concrete subclasses.
"""
from abc import ABC, abstractmethod
from share.program import Program

class ASCIIArtGenerator(Program, ABC):
    """
    Abstract base class for ASCII Art generators.

    This class inherits from Program and ABC, defining an abstract method 'generate'
    that must be implemented by concrete subclasses.
    """

    @abstractmethod
    def generate(self):
        """
        Abstract method to generate ASCII art.

        Concrete subclasses must implement this method to provide specific
        functionality for generating ASCII art.
        """
