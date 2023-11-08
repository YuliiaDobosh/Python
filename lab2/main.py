from .program import Program
from .color_calc import ColorCalculator

def main():
    calculator: Program = ColorCalculator()
    calculator.run()

if __name__ == "__main__":
    main()