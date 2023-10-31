from .shape import Shape
from ..graphic.graphic import Graphic

class Rectangle(Shape):
    def __init__(self, x1: int, y1: int, x2: int, y2: int, color: str, symbol: str) -> None:
        super().__init__(x1, y1, x2, y2, color, symbol)

    def display(self, graphic: Graphic):
        graphic.draw_line(self.x1, self.y1, self.x2, self.y1, self.color, self.symbol)
        graphic.draw_line(self.x1, self.y2, self.x2, self.y2, self.color, self.symbol)
        graphic.draw_line(self.x1, self.y1, self.x1, self.y2, self.color, self.symbol)
        graphic.draw_line(self.x2, self.y1, self.x2, self.y2, self.color, self.symbol)

        if self.color != "transparent":
            graphic.fill(self.x1 + 1, self.y1 + 1, self.x2 - 1, self.y2 - 1, self.color, self.symbol)
