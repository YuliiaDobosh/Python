"""
Calculator Module

This module provides a simple calculator implementation with basic arithmetic operations.

Classes:
    Calculator: A class that allows users to perform simple arithmetic calculations.

Functions:
    None

Usage:
    from calc import Calculator

    # Create an instance of the Calculator class
    calc = Calculator()

    # Run the calculator program
    calc.run()
"""

from .calc import Calculator

# Create an instance of the Calculator class and run the program
def main():
    """
    Entry point for the calculator program.

    This function creates an instance of the Calculator class and runs the
    calculator program.

    Usage:
        Run this script to start the calculator program.

    Returns:
        None
    """
    calc = Calculator()
    calc.run()

if __name__ == '__main__':
    main()
    