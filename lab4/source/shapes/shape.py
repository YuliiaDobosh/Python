from abc import ABC, abstractmethod
from ..graphic.graphic import Graphic

class Shape(ABC):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str, symbol: str) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.symbol = symbol
        super().__init__()

    @abstractmethod
    def display(self, graphic: Graphic):
        pass