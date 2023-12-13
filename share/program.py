"""
Module Description

This module defines the Program class, which serves as a base class for defining
program behavior. Derived classes can override the `run` method to implement specific
functionality.
"""

class Program:
    """
    Base Program class.

    This is a base class for defining program behavior. The `run` method should be
    overridden in derived classes to implement specific functionality.
    """
    def run(self):
        """
        Abstract method for running the program.

        This method should be overridden in derived classes to define the specific
        behavior of the program.
        """
        raise NotImplementedError("Subclasses must implement the 'run' method.")
    