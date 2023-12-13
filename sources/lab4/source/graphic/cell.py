from .color import Color

class Cell:
    def __init__(self, symbol, color='transparent') -> None:
        self.symbol = symbol
        self.color = color
