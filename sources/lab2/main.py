"""
Color Calculator Script

This script demonstrates the use of the ColorCalculator class from the color_calc module.
"""

from share.program import Program
from .color_calc import ColorCalculator

def main():
    """
    The main function of the script.

    Initializes a ColorCalculator and runs it.
    """
    calculator: Program = ColorCalculator()
    calculator.run()

if __name__ == "__main__":
    main()
